#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import base64				# built in python library for encoding/decoding
from Crypto.Cipher import AES		#built in python library for aes encryption/decryption
key=AES.new("choosetothinq321")	#key used:- choosetothinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("username")
pwd=fs.getvalue("password")
email=str(email).lower()
if email=="admin@webmaster.com" and str(pwd)=="admin12345":# check if the user is a administrator
	ans=json.dumps({"valid":[{"answer":"Administrator"}]})
else:
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	sql="SELECT COUNT(*) FROM `register` WHERE `Email`='%s' AND `Password`='%s';"%(str(email),str(pwd)) #check if email is registered
	con.execute(sql)
	res=con.fetchone()
	r=int(res[0])
	if r==1:
		temp=len(email)
		temp1=temp%16
		res=16-temp1
		for i in range(0,res):
			email=email+" "
		recv=key.encrypt(email)			#encrypt email to get token
		ans=json.dumps({"valid":[{"answer":"Authorised","email":base64.encodestring(recv)}]})
	else:
		ans=json.dumps({"invalid":[{"answer":"Unauthorised"}]})
	db.close()
print ans
