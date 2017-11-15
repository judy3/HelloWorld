#!/bin/bash

echo "USAGE EXAMPLE: $0 i-03e103abdff45b5cbi aws_profile"

PROFILE=${2:-"default"}
INS_ID=$1

PUB_IP=$(aws --profile $PROFILE ec2 describe-instances --instance-ids $INS_ID | jq -r '.Reservations[].Instances[].PublicIpAddress')
KEY=$(aws --profile $PROFILE ec2 describe-instances --instance-ids $INS_ID | jq -r '.Reservations[].Instances[].KeyName')
KEYNAME=$(echo ${KEY}.pem)

echo "ssh -i /home/judy/.ssh/keys/$KEYNAME ubuntu@$PUB_IP"

echo "ssh to the instance now..."
ssh -i /home/judy/.ssh/keys/$KEYNAME ubuntu@$PUB_IP
