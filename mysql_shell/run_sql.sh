#!/bin/bash

RDS_URL=$1
USER=$2
PASSWORD=$3
SQL_SCRIPT=$4
TABLE=$5

TEMP_PATH="/root/temp"
mkdir $TEMP_PATH
cp /tmp/$SQL_SCRIPT $TEMP_PATH/

echo "Install mysql client"
apt-get install mysql-client-core-5.7

echo "select * from $TABLE before update"
mysql -h${RDS_URL} -u${USER} -p"${PASSWORD}" << EOF  
 show databases;
 use platform;
 select * from ${TABLE};
EOF

echo "Update database ..."
mysql --force -h${RDS_URL} -u${USER} -p"${PASSWORD}" --database platform < $TEMP_PATH/$SQL_SCRIPT
echo "Update finished."

echo "select * from $TABLE after update"
mysql -h${RDS_URL} -u${USER} -p"${PASSWORD}" << EOF  
 show databases;
 use platform;
 select * from ${TABLE};
EOF

rm -rf $TEMP_PATH
