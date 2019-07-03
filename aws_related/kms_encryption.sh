#!/bin/bash

## This script is used to replace unencrypted EBS volumes to KMS encrypted ones of current running instances
## the usage is: ./kms_encryption.sh EC2_ID
## change the EC2_ID to actual EC2 id

EC2_ID=$1
PROFILE="--profile non-prod"  #change to your related aws configure file
TIME=$(date +"%F")
KMS_KEY_ID="put_the_KMS_key_id_here"
REGION="cn-north-1"  #change to the actual region

EC2_DETAILS=$(aws ec2 describe-instances $PROFILE --instance-ids $EC2_ID)
EC2_NAME=$(aws ec2 describe-tags $PROFILE --filters "Name=resource-id,Values=$EC2_ID" "Name=key,Values=Name" --output text | cut -f5 )
EC2_VOL_LIST=$(echo $EC2_DETAILS | jq -r '.Reservations[].Instances[].BlockDeviceMappings[].Ebs.VolumeId')

##Stop the EC2 server
echo "stopping the instance now..."
aws ec2 stop-instances $PROFILE --instance-ids $EC2_ID >>/dev/null


for VOL_ID in $EC2_VOL_LIST
do
  VOL_DETAILS=$(aws ec2 describe-volumes $PROFILE --volume-ids $VOL_ID)
  VOL_DEVICE=$(echo $VOL_DETAILS | jq -r '.Volumes[].Attachments[].Device')
  VOL_AZ=$(echo $VOL_DETAILS | jq -r '.Volumes[].AvailabilityZone')
  VOL_TYPE=$(echo $VOL_DETAILS | jq -r '.Volumes[].VolumeType' )
  VOL_SIZE=$(echo $VOL_DETAILS | jq -r '.Volumes[].Size')
  
  ## create the latest snapshot of the volume
  SNAPSHOT_1=$(aws ec2 create-snapshot $PROFILE --volume-id $VOL_ID --description "For_KMS_encryption" --tag-specifications "ResourceType=snapshot,Tags=[{Key=Name,Value=$EC2_NAME"_"$VOL_DEVICE"_"$TIME}]" | jq -r '.SnapshotId')

##copy it to a new encrypted snapshot  
  while true
  do
    SNAPSHOT_1_STATE=$(aws ec2 describe-snapshots $PROFILE --snapshot-id $SNAPSHOT_1 | jq -r '.Snapshots[].State')
	if [ x$SNAPSHOT_1_STATE != x"completed" ];then
		sleep 5s
	else
	SNAPSHOT_2=$(aws ec2 copy-snapshot $PROFILE --source-region $REGION --source-snapshot-id $SNAPSHOT_1 --description "
	$EC2_NAME"_"$VOL_DEVICE"_"$TIME" --encrypted --kms-key-id $KMS_KEY_ID | jq -r '.SnapshotId')
	break
	fi
  done
  
##Use this new snapshot to create an encrypted volume
  while true
  do
    SNAPSHOT_2_STATE=$(aws ec2 describe-snapshots $PROFILE --snapshot-id $SNAPSHOT_2 | jq -r '.Snapshots[].State')
	if [ x$SNAPSHOT_2_STATE == x"completed" ];then
	
	  NEW_VOL_ID=$(aws ec2 create-volume $PROFILE --availability-zone $VOL_AZ --encrypted --kms-key-id $KMS_KEY_ID --volume-type $VOL_TYPE --size $VOL_SIZE --snapshot-id $SNAPSHOT_2 --tag-specifications "ResourceType=volume,Tags=[{Key=Name,Value=$EC2_NAME"_"$VOL_DEVICE"_"$TIME}]" | jq -r '.VolumeId')
	  break
    else
      sleep 5s	
	fi
  done
  
#Check new volume status and replace the volume
  while true
  do
    NEW_VOL_STATUS=$(aws ec2 describe-volumes $PROFILE --volume-id $NEW_VOL_ID | jq -r '.Volumes[].State')
    CURRENT_EC2_STATE=$(aws ec2 stop-instances $PROFILE --instance-ids $EC2_ID | jq -r '.StoppingInstances[].CurrentState.Name')
    if [ $NEW_VOL_STATUS == "available" ] && [ $CURRENT_EC2_STATE == "stopped" ];then
      aws ec2 detach-volume $PROFILE --volume-id $VOL_ID
	    aws ec2 attach-volume $PROFILE --volume-id $NEW_VOL_ID --instance-id $EC2_ID --device $VOL_DEVICE
	  break
    fi
  done
  
done

echo "all the volumes has been replaced for EC2 $EC2_ID."

## after replacing, the old volumes and old snapshots can be deleted. I would suggest to keep those for some time in case any incidents happen.


