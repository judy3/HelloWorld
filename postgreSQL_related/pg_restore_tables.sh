#!/bin/bash
# This script is used to restore a single table from backup files in postgresql
# The script needs parameters to run: ./$0 $BAK_FILE $RESTORED_TABLE $NEW_TABLE
# Examaple: ./$0 table1_2019-08-20.pgsql table1 table1_20190820

#check if the input parameters are enough or not
if [ "$#" != "3" ]
 then
        echo "Please make sure you've put enough/correct parameters!"
		echo "Examaple: ./$0 table1_2019-08-20.pgsql table1 table1_20190820"
		echo "PLEASE NOTE: "-" is not accepted in the table name"
        exit 1
fi

echo "going to restore..."
#restore the table to a new table in postgresql
BAK_DIR="/distination_dir/pg_tables_backup"
BAK_FILE=$1
RESTORED_TABLE=$2
NEW_TABLE=$3
NEW_BAK_FILE=$BAK_DIR"/tableNameChanged_"$BAK_FILE

#change the table name in the backup file(sql plain text)
sed "s/$RESTORED_TABLE/$NEW_TABLE/ig" $BAK_DIR/$BAK_FILE > $NEW_BAK_FILE

function pg_restore_table()
{
PG_HOST="localhost"
PG_PORT="5432"
PG_USER="user1"
PG_DATABASE="database1"

#the pgsql password is saved in the file ~/.pgpass, ref: https://www.postgresql.org/docs/9.3/libpq-pgpass.html
psql -h $PG_HOST -p $PG_PORT -U $PG_USER -d $PG_DATABASE < $1
}

pg_restore_table $NEW_BAK_FILE

echo "Table $NEW_TABLE restore completed."
