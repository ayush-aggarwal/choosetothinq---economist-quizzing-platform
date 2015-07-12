#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import base64							#built in python library for encoding/decoding
from Crypto.Cipher import AES			#built in python library to provide encryption
key=AES.new("choosetothinq321")			#key used :- choosetothinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
name=fs.getvalue("name")
email=fs.getvalue("email")
gender=fs.getvalue("gender")
image=fs.getvalue("image")
email=str(email).lower()
encryemail=email						
temp=len(encryemail)
temp1=temp%16
res=16-temp1
for i in range(0,res):
	encryemail=encryemail+" "
recv=key.encrypt(encryemail)			#encrypting email to get token
try:
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	sql="SELECT COUNT(*) FROM `register` WHERE `Email`='%s';"%(str(email))
	con.execute(sql)
	res=con.fetchone()
	r=int(res[0])
	if r==0:
		sql1="INSERT INTO `register`(`Full Name`,`Email`,`Password`,`Country`,`Total Score`,`No_of_games`,`Average Score`) VALUES ('%s','%s','%s','%s','%d','%d','%f');"%(str(name),str(email),str("#fbuser"),str("Not Available"),int(0),int(0),0)
		con.execute(sql1)
		db.commit()
		ans=json.dumps({"valid":[{"answer":"success","email":base64.encodestring(recv)}]})
	elif r==1:
		ans=json.dumps({"valid":[{"answer":"success","email":base64.encodestring(recv)}]})
	else:
		ans=json.dumps({"invalid":[{"answer":"fail"}]})
except:
	ans=json.dumps({"invalid":[{"answer":"fail"}]})
print ans
