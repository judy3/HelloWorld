#!/bin/bash

# This script is used to start an EC2 instance which is stopped at the moment and ssh to the instance

#to make sure the clock is correct

INS_ID="i-xxxxxxxxxxx"
aws ec2 start-instances --instance-ids $INS_ID

while :
do
        echo "checking the instance state..."
        STATE=$(aws ec2 describe-instances --instance-ids $INS_ID | jq -r ".Reservations[].Instances[].State.Name")
        if [ $STATE = "running" ];then
                echo "print the public IP"
                PUB_IP=$(aws ec2 describe-instances --instance-ids $INS_ID | jq -r ".Reservations[].Instances[].PublicIpAddress")
                echo $PUB_IP
                echo "ssh to the instance"
                ssh -i /home/judy/.ssh/judykey.pem ubuntu@$PUB_IP
                exit 0
        fi
done

