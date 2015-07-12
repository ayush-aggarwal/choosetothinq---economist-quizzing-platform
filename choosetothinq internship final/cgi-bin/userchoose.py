#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import base64	#built in python module for encoding/decoding
from Crypto.Cipher import AES	#built in python module for aes encryption
key=AES.new("choosetothinq321")	#key used: - choosetothinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
try:
	email=fs.getvalue("email")
	recv=base64.decodestring(email)
	email=key.decrypt(recv)	#decrypt token to get email
	email=str(email).strip()
	dic={}
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	sql="SELECT `Full Name`,`Email`,`Country`,`Total Score`,`No_of_games`,`Average Score` FROM `register` WHERE `Email`='%s';"%(str(email))#get details of user for the email given
	con.execute(sql)
	res=con.fetchone()
	dic["name"]=str(res[0])
	dic["email"]=str(res[1])
	dic["country"]=str(res[2])
	dic["total_score"]=str(res[3])
	dic["no_of_games"]=str(res[4])
	dic["average_score"]=str(res[5])
	ans=json.dumps({"valid":[dic],"email":str(email)})
	db.close()
	print ans
except:
	pass
