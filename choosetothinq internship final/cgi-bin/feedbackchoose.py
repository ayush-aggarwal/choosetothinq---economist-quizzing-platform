#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue('email')
name=fs.getvalue('name')
message=fs.getvalue('message')
email=str(email).lower()
if str(message)!="None":		#check if message is empty
	try:
		db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
		con=db.cursor()
		sql="INSERT INTO `feedback` (`Name`,`Email`,`Message`) VALUES ('%s','%s','%s');"%(str(name),str(email),str(message))
		con.execute(sql)
		db.commit()
		print "Success"
	except:
		print "Fail"
db.close()
