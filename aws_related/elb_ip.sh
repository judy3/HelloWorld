#!/bin/bash

echo "USAGE: $0 load-balancer-name aws_profile"
echo "OUTPUT FORMAT: EC2 ID :: IP :: TYPE :: LIFECYCLE"

PROFILE=${2:-"default"}
ELB=$1

aws --profile $PROFILE elb describe-instance-health --load-balancer-name $ELB | jq -r '.InstanceStates[].InstanceId' > instanceid.txt
EC2NUM=$(cat instanceid.txt | wc -l)

i=1
while [ $i -le $EC2NUM ]
do
  EC2_ID=$(sed -n $i'p' instanceid.txt)
  aws --profile $PROFILE ec2 describe-instances --instance-ids $EC2_ID > instance.json
  INSTANCE_IP=$(cat instance.json | jq -r '.Reservations[].Instances[].PublicIpAddress')
  EC2_TYPE=$(cat instance.json | jq -r '.Reservations[].Instances[].InstanceType')
  EC2_TYPE2=$(cat instance.json | jq -r '.Reservations[].Instances[].InstanceLifecycle')
  echo "$EC2_ID :: $INSTANCE_IP :: $EC2_TYPE :: $EC2_TYPE2"
(( i++ ))
done
