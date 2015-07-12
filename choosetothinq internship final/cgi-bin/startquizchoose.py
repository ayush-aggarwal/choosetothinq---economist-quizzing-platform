#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import urllib2
import base64	#built in python library for encoding/decoding
from Crypto.Cipher import AES	#built in python library for aes encryption/decryption
key=AES.new("choosetothinq321")	#key used:- choosetothinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("username")
recv=base64.decodestring(email)
email=key.decrypt(recv)	#decrypt token to get email
email=str(email).strip()
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
try:
	sql="SELECT * FROM `register` WHERE `Email`='%s';"%(str(email))#check if email is  registered
	con.execute(sql)
	res=con.fetchone()
	name=str(res[0])
	sql1="INSERT INTO `game` (`Name`,`Email`,`Score`) VALUES('%s','%s','%d');"%(str(name),str(email),0)#insert player details into current playing players tables i.e game table
	con.execute(sql1)
	db.commit()
	ans=json.dumps({"valid":[{"noanswer":"Success"}]})
except:
	ans=json.dumps({"invalid":[{"noanswer":"Fail"}]})
db.close()
print ans
