CODE
'''
Google account
smartrasp3@gmail.com
raspberrypi@3
'''

import time
import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from twilio.rest import TwilioRestClient

directory_id = '0BxI-jlB8cnRGanhNMTJwSVZ3WGc'

defsendSMS(body):
	ACCOUNT_SID = "AC2a7f1002527a72bc507c40423e181255"
	AUTH_TOKEN = "77b9a6e44c1c0eb1bd240e695e159d93"
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	mes = client.messages.create(to="+918010257683", from_="+1 415-599-2671", body=body)
	print  'SMS Send. Details: ',
	print mes

gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
	# Authenticate if they're not there
	gauth.LocalWebserverAuth()
elifgauth.access_token_expired:
	# Refresh them if expired
	gauth.Refresh()
else:
	# Initialize the saved creds
	gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

number_of_files = 0
ppt_list = []
while True:
	# Auto-iterate through all files that matches this query
	file_list = drive.ListFile({'q': "'" + directory_id + "' in parents and trashed=false"}).GetList()
	tmp = []
	for item in file_list:
		if 'presentation' in item['mimeType']:
			t = {"title":item['title'], "id": item['id']}
			tmp.append(t)
			#print '# ' + item['title']
	flag = False
	msg = ''
	for item in tmp:
		if {"title":item['title'], "id": item['id']} not in ppt_list:
			flag = True
			print item['title'],
			print 'received'
			msg += item['title'] + ', '
	
	if flag:
		msg = msg[:-2]
		sendSMS("Received files: " + msg)
		print '-------------------------------------------------'
	
	number_of_files = len(file_list)
	ppt_list = tmp
	time.sleep(5)
































