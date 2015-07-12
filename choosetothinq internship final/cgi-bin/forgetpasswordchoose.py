#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import urllib2
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("username")
email=str(email).lower()
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
try:
	sql="SELECT COUNT(*) FROM `register` WHERE `Email`='%s';"%(str(email))
	con.execute(sql)
	res=con.fetchone()
	r=int(res[0])
	if r==0:			
		ans=json.dumps({"invalid":[{"answer":"Email Not Registered"}]})
	else:
		ans=json.dumps({"valid":[{"answer":"OK"}]})
except:
	ans=json.dumps({"invalid":[{"answer":"Email Not Registered"}]})
db.close()
print ans
