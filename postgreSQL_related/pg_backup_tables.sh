#!/bin/bash

# This script is used to backup two postgresql tables: table1 table2 table3
# The script is running on the pgSql server which installed pgsql client

function pg_backup_table()
{
PG_HOST="localhost" #change the hostname here
PG_PORT="5432" #this is the default port, change to the port you used
PG_USER="user1"
PG_DATABASE="database1"

DATE=`date +"%F"`
BAK_FILE=$1"_"$DATE".pgsql"

#the pgsql password is saved in the file ~/.pgpass, ref: https://www.postgresql.org/docs/9.3/libpq-pgpass.html
pg_dump -h $PG_HOST -p $PG_PORT -U $PG_USER -d $PG_DATABASE -t $1  > $2/$BAK_FILE

}

function clean_old_backups()
{
#delete files older than 5 days with extension .pgsql
find $1 -mtime +5 -name "*.pgsql" -exec rm -rf {} \;
}

TABLES="table1 table2 table3"
BAK_DIR="/distination_dir/pg_tables_backup"

for table in $TABLES
do

	echo "backing up table $table ..."
	pg_backup_table $table $BAK_DIR
	echo "Table $table backup finished."
	
done

echo "cleaning backup files older than 5 days"
clean_old_backups $BAK_DIR
echo "cleanup finished."

#create cron job for this script in order to backup those tables everyday
