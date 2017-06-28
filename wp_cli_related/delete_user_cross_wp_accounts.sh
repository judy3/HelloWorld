#!/bin/bash
#This sropt is used to delete a same user in every wordpress server

user_email="tested.user@example.com"
reassign_user_email="judy3.yang@example.com"

wordpress_path="/var/www/wordpress"

#Host is already configed in the /home/judy/.ssh/config 
#example host: web_dev web_stage web_prod

for host in web_dev web_stage web_prod; do
	user_name_net=$(wp --ssh="$host" --path="$wordpress_path" user list --network --fields=ID,user_login,user_email | grep -i $user_email | awk '{print $2}')
	user_name=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $user_email | awk '{print $2}')
	if [ $user_name_net ]; then
		echo "$host :: there's still user $user_name_net in the network"
		if [ $user_name ]; then
			echo "deleting $user_name and reassign posts to $reassign_user ..."
			reassign_user_id=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $reassign_user_email | awk '{print $1}')
			reassign_user=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $reassign_user_email | awk '{print $2}')
			wp --ssh="$host" --path="$wordpress_path" user delete "$user_name_net" --reassign="$reassign_user_id"
		fi
		echo "checking if it's super admin..."
		super_admin=$(wp --ssh="$host" --path="$wordpress_path" super-admin list | grep -i $user_name_net)
		if [ $super_admin ];then
			echo "On $host , $user_name_net is still the super admin and revoke the capacity now..."
			wp --ssh="$host" --path="$wordpress_path" super-admin remove $super_admin
			else
				echo "On $host , $user_name_net is not the super admin"
		fi
		echo "ATTENTION:: on $host , deleting $user_name_net on the network manually"
		##not sure how to delete user and reassign posts in multiple sites
		##When tried to `wp user delete --network tested.username --reassign=38` , got the Error: Reassigning content to a different user is not supported on multisite.
		##Please let me know if there's any better way to delete
		
		else 
			echo "there's no $user_email in the $host"
	fi
done
