import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

directory_id = '0BxI-jlB8cnRGanhNMTJwSVZ3WGc'

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

print 'Available presentations'
file_list = drive.ListFile({'q': "'" + directory_id + "' in parents and trashed=false"}).GetList()
for item in file_list:
	if 'presentation' in item['mimeType']:
		print item['title']
filename = raw_input('enter filename to open: ')
for item in file_list:
	if item['title'] == filename:
		print 'Found:',
		print item['title'], '(id =' + item['id'] + ')'
		getppt = drive.CreateFile({'id': item['id']}) # Initialize GoogleDriveFile instance with file id
		getppt.GetContentFile(item['title']) # Download file as 'catlove.png'
		print 'Download Complete'
		print 'Opening ' + item['title']
		os.system("soffice " + item['title'])
		break
print 'Exiting'
