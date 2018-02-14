# -*- coding: utf-8 -*-
import configparser;
import urllib.request, json;
import MySQLdb; 
import smtplib;
import sys;

config = configparser.ConfigParser();
configcontent = config.read('config.ini');
sections = config.sections()
#print(sections)

def sendemail(subject,text):
	SUBJECT = subject
	TEXT = text;
	sender = "kashif.khan@tavant.com"
	smtp = config['email'].get('smtp');
	port = config['email'].get('url');
	TO = config['email'].get('to');
	server = smtplib.SMTP(smtp, port);
	BODY = '\r\n'.join(['To: %s' % TO,
                    'From: %s' % sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])
	try:
		server.sendmail(sender, [TO], BODY)
		print ('email sent')
	except Exception as e:
		print ('error sending mail');
		print(e)

	server.quit()				


# Url from where we load the Json data
url = config['url'].get('url');

#load the data from URL
try:
	with urllib.request.urlopen(url) as url:
		readData = url.read();
		#print(readData);
		
		decodeData = readData.decode();
		data = json.loads(decodeData);
		#data = json.dumps(readData).decode('unicode-escape').encode('utf8')
		#print(data)
except ValueError as v:
		print('Some Invalid Url error');	

insertlist = [];
# Function for generation of the list , that will be inserted in database
def generateListForInsertion(jsonDataFromFile):
	for jsonData in jsonDataFromFile:
		gender = jsonData['gender'].capitalize();
		#name="";
		#address="";
		name = jsonData['name']['title']+" "+jsonData['name']['first']+" "+jsonData['name']['last'];
		name = name.encode('utf-8')
		address = jsonData['location']['street']+" "+jsonData['location']['city']+" "+jsonData['location']['state'];
		
		#print(address)
		address = address.encode('utf-8')
		#print(address)
		insertlist.append((gender,name,address));
		
generateListForInsertion(data['results']);
#print(insertlist)
		



def _createConnection():
	try:
		# Data base configurations
		global connection;
		global cursor;
		host = config['database'].get('host');
		username = config['database'].get('username');
		password = config['database'].get('password');
		databasename = config['database'].get('databasename');
		connection = MySQLdb.connect(host,username,password,databasename);
		cursor = connection.cursor();
		cursor.execute("set names utf8;")
		#print(connection);
	except MySQLdb.Error as e:
			print("Connection problem");
			sendemail("Connection problem","There is some database connection problem");
			sys.exit(1)

def _insertData(insertlist):
	query = "INSERT INTO jsondata(gender,name,address) " \
			"VALUES(%s,%s,%s)"
	try:
		cursor.executemany(query, insertlist);
		connection.commit();
	except MySQLdb.Error as e: 
		print("Execution error");
		sendemail("Execution error","There is some issue in execution of query");

def fetchData():
	query = "select name from jsondata limit 1,2";
	cursor.execute(query)
	user = cursor.fetchone()[0];
	print(user)
	#print(user.encode('latin-1'))
    #return user
			
_createConnection();
#fetchData();
_insertData(insertlist)
