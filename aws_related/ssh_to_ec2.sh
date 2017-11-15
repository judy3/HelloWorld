#!/bin/bash

echo "USAGE EXAMPLE: $0 i-03e103abdff45b5cbi aws_profile"

PROFILE=${2:-"default"}
INS_ID=$1

aws --profile $PROFILE ec2 describe-instances --instance-ids $INS_ID > ssh_info.json

PUB_IP=$(cat ssh_info.json | jq -r '.Reservations[].Instances[].PublicIpAddress')
KEY=$(cat ssh_info.json | jq -r '.Reservations[].Instances[].KeyName')
KEYNAME=$(echo ${KEY}.pem)

echo "ssh -i /home/judy/.ssh/keys/$KEYNAME ubuntu@$PUB_IP"

echo "ssh to the instance now..."
ssh -i /home/judy/.ssh/keys/$KEYNAME ubuntu@$PUB_IP
