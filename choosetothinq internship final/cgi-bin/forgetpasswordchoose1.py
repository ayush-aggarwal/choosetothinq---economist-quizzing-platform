#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("username")
email=str(email).lower()
password=fs.getvalue("password")
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
try:
	if(len(str(password))<8):
		ans=json.dumps({"invalid":[{"answer":"** Password Must be 8 or more characters"}]})
	else:
		sql1="INSERT INTO `forgetpasswordrequest`(`Email`,`Password`) VALUES('%s','%s');"%(str(email),str(password))
		con.execute(sql1)
		db.commit()
		ans=json.dumps({"valid":[{"answer":"Success"}]})
except:
	ans=json.dumps({"invalid":[{"answer":"** Maybe Your previous request is pending. Sorry for Inconvenience."}]})
db.close()
print ans
