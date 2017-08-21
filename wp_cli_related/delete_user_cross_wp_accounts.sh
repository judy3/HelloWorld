#!/bin/bash
#This sropt is used to delete a same user in every wordpress server

user_general_name="testuser"
reassign_user_email="Judy3.Yang@gmail.com"

for wordpress_path in "/var/www/thestsite/www" "/var/www/wordpress"; do
	if [ $wordpress_path = "/var/www/testsite/www" ];then
		for host in test-dev1 test-stage1 test-prd1; do
			echo "checking user on $host ..."
			
			super_admin=$(wp --ssh="$host" --path="$wordpress_path" super-admin list | grep -i $user_general_name)
			user_name=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $user_general_name | awk '{print $2}')
			user_name_net=$(wp --ssh="$host" --path="$wordpress_path" user list --network --fields=ID,user_login,user_email | grep -i $user_general_name | awk '{print $2}')
			reassign_user=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $reassign_user_email | awk '{print $2}')
			
			if [ $super_admin ];then
				 echo "On $host , $user_general_name is a super admin and revoke the capacity now..."
                 wp --ssh="$host" --path="$wordpress_path" super-admin remove $super_admin
				 echo "please manually delete user on network"
				 if [ $user_name ];then
					echo "Deleting user on site ..."
					wp --ssh="$host" --path="$wordpress_path" user delete "$user_name_net" --reassign="$reassign_user" 
				 elif [ $user_name_net ];then
					echo "Deleting user on the site..."
					wp --ssh="$host" --path="$wordpress_path" user delete --network "$user_name" --reassign="$reassign_user" 
				 fi
			else
				if [ $user_name ];then
					echo "Deleting user on the site and reassign posts to $reassign_user..."
					wp --ssh="$host" --path="$wordpress_path" user delete "$user_name" --reassign="$reassign_user"
				elif [ $user_name_net ];then
					echo "Deleting user on multiple sites..."
					wp --ssh="$host" --path="$wordpress_path" user delete --network "$user_name" --reassign="$reassign_user"
				fi
			fi
		done
	else
		for host in site1 site2 site3; do
			echo "checking user on $host ..."
			
			super_admin=$(wp --ssh="$host" --path="$wordpress_path" super-admin list | grep -i $user_general_name)
			user_name=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $user_general_name | awk '{print $2}')
			user_name_net=$(wp --ssh="$host" --path="$wordpress_path" user list --network --fields=ID,user_login,user_email | grep -i $user_general_name | awk '{print $2}')
			reassign_user=$(wp --ssh="$host" --path="$wordpress_path" user list --fields=ID,user_login,user_email | grep -i $reassign_user_email | awk '{print $2}')
			
			if [ $super_admin ];then
				 echo "On $host , $user_general_name is a super admin and revoke the capacity now..."
                 wp --ssh="$host" --path="$wordpress_path" super-admin remove $super_admin
				 echo "please manually delete user on network"
				 if [ $user_name ];then
					echo "Deleting user on site ..."
					wp --ssh="$host" --path="$wordpress_path" user delete "$user_name_net" --reassign="$reassign_user" 
				 elif [ $user_name_net ];then
					echo "Deleting user on the site..."
					wp --ssh="$host" --path="$wordpress_path" user delete --network "$user_name" --reassign="$reassign_user" 
				 fi
			else
				if [ $user_name ];then
					echo "Deleting user on the site and reassign posts to $reassign_user..."
					wp --ssh="$host" --path="$wordpress_path" user delete "$user_name" --reassign="$reassign_user"
				elif [ $user_name_net ];then
					echo "Deleting user on multiple sites..."
					wp --ssh="$host" --path="$wordpress_path" user delete --network "$user_name" --reassign="$reassign_user"
				fi
			fi
		done
	fi
done
