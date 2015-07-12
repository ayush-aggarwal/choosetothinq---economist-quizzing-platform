#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import base64					#python built in library for encoding/decoding
from Crypto.Cipher import AES	#python built in library for aes encryption/decryption
key=AES.new("choosetothinq321") # key used :- choosetothhinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("email")
id1=fs.getvalue("id")
ans=fs.getvalue("ans")
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
sql="SELECT `correctans` FROM `questions` WHERE `id`='%d';"%(int(id1)) #get correctans
con.execute(sql)
res=con.fetchone()
answer=str(res[0])
if str(ans)==answer:	#check correctanswer
	recv=base64.decodestring(email)
	email=key.decrypt(recv)	#decrypt token to get email
	email=str(email).strip()
	sql1="UPDATE `game` SET `Score`=`Score`+10 WHERE `Email`='%s';"%(str(email))	# give user 10 points for correct answer 
	con.execute(sql1)
	db.commit()
	abc=json.dumps({"valid":[{"answer":"success"}]})
else:
	abc=json.dumps({"invalid":[{"answer":answer}]})	#return correct answer if the user answered wrong
db.close()
print abc
