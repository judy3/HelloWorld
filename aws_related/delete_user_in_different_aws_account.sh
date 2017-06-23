#!/bin/bash

# to delete a same IAM user based on all aws accounts

staff="judy"
profiles=(web_dev web_stage web_prod) ##profile for each aws account
for aws_profile in "${profiles[@]}"
do
        echo $aws_profile
        name=`aws --profile $aws_profile iam list-users | jq -r '.Users[].UserName' | grep -i ${staff}`
        echo $name
        if [ $name ];then
                access_key_id=`aws --profile $aws_profile iam list-access-keys --user-name $name | jq -r '.AccessKeyMetadata[].AccessKeyId'`
                if [ $access_key_id ];then
					echo "deleting the access-key..."
					aws --profile $aws_profile iam delete-access-key --access-key $access_key_id --user-name $name
				fi
                CertificateId=`aws --profile $aws_profile iam  list-signing-certificates --user-name $name | jq -r '.Certificates[].CertificateId'`
                if [ $CertificateId ];then
					echo "deleting the signing-certificate..."
					aws --profile $aws_profile iam delete-signing-certificate --user-name $name --certificate-id $CertificateId
				fi
				login_profile=`aws --profile $aws_profile iam get-login-profile --user-name $name | jq -r '.[].UserName' `
				if [ $login_profile ];then
				echo "deleting the login-profile..."
				aws --profile $aws_profile iam delete-login-profile --user-name $name 
				fi
				MFA=`aws --profile $aws_profile iam list-mfa-devices --user-name $name | jq -r '.MFADevices[].SerialNumber'`
				if [ $MFA ];then
					echo "deactivate-mfa-device..."
					aws --profile $aws_profile iam deactivate-mfa-device --user-name $name --serial-number $MFA
				fi
				attached_policies=(`aws --profile $aws_profile iam list-attached-user-policies --user-name $name | jq -r '.AttachedPolicies[].PolicyArn'`)
				if [ $attached_policies ];then
					for policy in "${attached_policies[@]}"
					do
						echo "detach-user-policy..."
						aws --profile $aws_profile iam detach-user-policy --user-name $name --policy-arn $policy
					done
				fi
				inline_policies=(`aws --profile $aws_profile iam list-user-policies --user-name $name | jq -r '.PolicyNames[]'`)
				if [ $inline_policies ];then
					for inline_policy in "${inline_policies[@]}"
					do
						echo "delete-user-inline_policies..."
						aws --profile $aws_profile iam delete-user-policy --user-name $name --policy-name $inline_policy
					done
				fi
				user_groups=(`aws --profile $aws_profile iam list-groups-for-user --user-name $name | jq -r '.Groups[].GroupName'`)
				if [ $user_groups ];then
					for group in "${user_groups[@]}"
					do
						echo "deleting user from his group..."
						aws --profile $aws_profile iam remove-user-from-group --user-name $name --group-name $group
					done
				fi
				ssh_public_keys=(`aws --profile $aws_profile iam list-ssh-public-keys --user-name $name | jq -r '.SSHPublicKeys[].SSHPublicKeyId'`)
				if [ $ssh_public_keys ];then
					for key in "${ssh_public_keys[@]}"
					do
						echo "delete-user-ssh_public_keys..."
						aws --profile $aws_profile iam delete-ssh-public-key --user-name $name --ssh-public-key-id $key
					done
				fi 
				echo "deleting user..."
				aws --profile $aws_profile iam delete-user --user-name $name
        fi
done