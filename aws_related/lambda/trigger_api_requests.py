# This is python 3 code for AWS lambda that triggered by S3 put object. It will read the text object and send out to an appliction.(API here)

import json
import urllib.parse
import boto3

from botocore.vendored import requests   
#Because the requests model was not intalled in the root zip file, so need to import it from botocore,vendored; otherwise to install it with the command: pip install requests -t ./

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
	
	bucket = event['Records'][0]['s3']['bucket']['name']
	key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
	try:
		data = s3.get_object(Bucket=bucket, Key=key)
		contents = data['Body'].read()   # The contents will be bytes type
		print("contents is {}".format(contents))   
		encoding = 'utf-8'
		message = str(contents, encoding)   #convert the bytes type to string
		print("message is {}".format(message))
		api_url = "https://you-application.com/api"   #change this part to the api url
		token_url = api_url + "/your/token/path/here"    # this is to get the token, this part needs to be modified according to the api document
		#change the token request json file if different, the type of it is dict, by default python 3 cannot convert byte to json
		token_request = {
			"grant_type": "client_credentials",
			"scope": "app",
			"domain_id": "your_domain",
			"org_id": "your_orgnization_id",
			"client_id": "your_client_id",
			"client_secret": "your_client_secred"
			}
		print(type(token_request))
    
    #change the headers if different
		headers = {
			"Content-type": "application/json"
			}
      
    # this is post HTTP request, note to convert the dict to json
		response = requests.post(token_url, headers = headers, data = json.dumps(token_request))
    # this is to get the value of access_token in the json response, change it if different from your api response
		token = json.loads(response.text)['result']['access_token']
		print("token is {}." .format(token))
		# send out the message
    
    # this is the to publish message url, change it according to your api
		send_url = api_url + "/your/path/here?access_token=" + token
		#content = "line1 \n line2 \n test message, please ignore it \n"
    
    # message receiver
		receivers = ["username1", "username2"]
    # change the send requst json according to your api requirement
		send_request = {
			"type": "TEXT",
			"body": {
				"content": message
				},
			"usernames": receivers,
			"platforms": ["ANDROID", "IOS", "PC"]
			}
		print(type(send_request))
		sendOut_reponse = requests.post(send_url, headers = headers, data = json.dumps(send_request))
		print(sendOut_reponse.text)   
       
	except Exception as e:
		print(e)
		print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
		raise e
