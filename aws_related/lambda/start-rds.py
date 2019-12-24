import logging
import boto3

rds_client = boto3.client('rds')
dbs = rds_client.describe_db_instances()

def lambda_handler(event, context):
    def get_tags_for_db(db):
        instance_arn = db['DBInstanceArn']
        instance_tags = rds_client.list_tags_for_resource(ResourceName=instance_arn)
        return instance_tags['TagList']
    
    for db in dbs['DBInstances']:
        db_tags = get_tags_for_db(db)
        db_status = db['DBInstanceStatus']
        db_identifier = db['DBInstanceIdentifier']
        for tag in db_tags:
            if tag['Key'] == 'AUTOOFF' and tag['Value'] == 'TRUE' and db_status == 'stopped':
                print("%s will start now." % db_identifier )
                rds_client.start_db_instance(DBInstanceIdentifier=db_identifier)
            '''
            # below snippet is to stop rds instances
            if tag['Key'] == 'AUTOOFF' and tag['Value'] == 'TRUE' and db_status == 'available':
                print("%s will stop now." % db_identifier )
                rds_client.stop_db_instance(DBInstanceIdentifier=db_identifier)   
            '''
          
 # This lambda function is to do RDS instances(not the Aurora Cluster) auto start and stop based on the Cloudwatch event.
