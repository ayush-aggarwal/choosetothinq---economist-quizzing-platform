#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import urllib2
import base64					#built in python library for encoding decoding
from Crypto.Cipher import AES	#built in python library for aes encryption
key=AES.new("choosetothinq321") #key used:- choosetothinq321 (16 bit)
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
email=fs.getvalue("email")
recv=base64.decodestring(email)
email=key.decrypt(recv)		#decrypt token to get email
email=str(email).strip()
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
try:
	sql="DELETE FROM `game` WHERE `Email`='%s';"%(str(email)) #remove the player from current playing player table i.e game table
	con.execute(sql)
	db.commit()
	print "ok"
except:
	print "not ok"

