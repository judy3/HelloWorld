#!/bin/bash

echo "USAGE: $0 load-balancer-name aws_profile"
echo "OUTPUT FORMAT: EC2 ID :: IP"
##This is used for: Get the instance IDs and IPs of an ELB

PROFILE=${2:-"default"}
ELB=$1

aws --profile $PROFILE elb describe-instance-health --load-balancer-name $ELB | jq -r '.InstanceStates[].InstanceId' > instanceid.txt
EC2NUM=$(cat instanceid.txt | wc -l)

i=1
while [ $i -le $EC2NUM ]
do
  EC2_ID=$(sed -n $i'p' instanceid.txt)
  INSTANCE_IP=$(aws --profile $PROFILE ec2 describe-instances --instance-ids $EC2_ID | jq -r '.Reservations[].Instances[].PublicIpAddress')
  echo "$EC2_ID :: $INSTANCE_IP"
(( i++ ))
done
