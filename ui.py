from Tkinter import *
import time
import json
import math
import threading
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from twilio.rest import TwilioRestClient

screen_width = 800
screen_height = 400

directory_id = '0BxI-jlB8cnRGanhNMTJwSVZ3WGc'
credfile = 'mycreds.txt'
app_name = 'Smartclass 1.0'

class Application(Frame):
	defsendSMS(self, body):
		ACCOUNT_SID = "AC2a7f1002527a72bc507c40423e181255"
		AUTH_TOKEN = "77b9a6e44c1c0eb1bd240e695e159d93"
		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
		mes = client.messages.create(to="+918010257683", from_="+1 415-599-2671", body=body)
		print  'SMS Send. Details: ',
		print mes
	
	defsay_hi(self, name):
	print "hi there, ", name		
	
	deftrigger(self, filename):
		cmd = "python downloader.py " + filename
		os.system(cmd)

	deffile_type(self, filetype):
		if 'presentation' in filetype:
			return 'ppt'
		elif 'document' in filetype:
			return 'doc'
		elif 'spreadsheet' in filetype:
			return 'xls'
		return 'other'                
	
	defcronjob(self):		
		gauth = GoogleAuth()
		# Try to load saved client credentials
		gauth.LoadCredentialsFile(credfile)
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
		gauth.SaveCredentialsFile(credfile)
		
		drive = GoogleDrive(gauth)
		
		number_of_files = 0
		ppt_list = []
		ppt_list_json = {}
		while True:
			# Auto-iterate through all files that matches this query
			file_list = drive.ListFile({'q': "'" + directory_id + "' in parents and trashed=false"}).GetList()
			tmp = []
			for item in file_list:
				#if 'presentation' in item['mimeType']:
				t = {"title":item['title'], "id": item['id'], 'mimeType': self.file_type(item['mimeType'])}
				tmp.append(t)
		
			flag = False
			msg = ''
			for item in tmp:
				if {"title":item['title'], "id": item['id'], 'mimeType': item['mimeType']} not in ppt_list:
					flag = True
					print item['title'],
					print 'received'
					msg += item['title'] + ', '
			
			if flag:
				msg = msg[:-2]
				#self.sendSMS("Received files: " + msg)
				print 'SMS sent.'
				if number_of_files != 0:
					self.grid_forget()
		self.grid(padx=20,pady=100)
		self.createWidgets(tmp)
				print 'UI Updated'
				print '-------------------------------------------'  
		
			number_of_files = len(file_list)
			ppt_list = tmp
			time.sleep(5)		

	defcreateWidgets(self, data):
		#self.mytitle = Label(root, text=app_name)
		#self.mytitle.config(font=('times', 20, 'bold'))
		#self.mytitle.grid(row=0,column=0, sticky=W)

		self.image_ppt = PhotoImage(file="ppt.png")
		self.image_doc = PhotoImage(file="doc.png")
		self.image_xls = PhotoImage(file="xls.png")
		self.image_other = PhotoImage(file="other.png")
		i = 7
		j= 0
		for item in data:
			if 'ppt' in item['mimeType']:
				self.image = self.image_ppt
	elif 'doc' in item['mimeType']:
	self.image = self.image_doc
	elif 'xls' in item['mimeType']:
self.image = self.image_xls
			else:
				self.image = self.image_other
			self.newmessage = Button(self, compound=TOP, text= item['title'], anchor=W, image=self.image, command = lambda i=item['title']:self.trigger(i))
			self.newmessage.config(height = 70, width = 64)
			self.newmessage.grid(column = j, row = i, sticky = NW)
			j += 1
			if(j == 8):
				i += 1
				j = 0
	
	def __init__(self, master=None):
	Frame.__init__(self, master)
	t = threading.Thread(target=self.cronjob)
	try:
		t.start()
	except (KeyboardInterrupt, SystemExit):
		t.stop()

if __name__ == '__main__':
	root = Tk()
	root.geometry('{}x{}'.format(screen_width, screen_height))
	app = Application(master=root)
	root.title(app_name)
	root.mainloop()
	root.destroy()
