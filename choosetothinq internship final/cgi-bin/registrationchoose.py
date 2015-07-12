#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import urllib2
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
name=fs.getvalue("fullname")
email=fs.getvalue("username")
password=fs.getvalue("password")
rpassword=fs.getvalue("rpassword")
country=fs.getvalue("country_id")
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
email=str(email).lower()
try:
	sql="SELECT COUNT(*) FROM `register` WHERE `Email`='%s';"%(str(email))	#check if email is not already registered
	con.execute(sql)
	res=con.fetchone()
	res1=int(res[0])
	if(res1==0):
		sql1="INSERT INTO `register`(`Full Name`,`Email`,`Password`,`Country`,`Total Score`,`No_of_games`,`Average Score`) VALUES ('%s','%s','%s','%s','%d','%d','%f');"%(str(name),str(email),str(password),str(country),0,0,0)
		con.execute(sql1)
		db.commit()
		msg="Successfully Registered"
	else:
		msg="Your Email is already registered"
except:
	msg="Sorry Could'nt Register!!Please Try Again"
db.close()
print msg
