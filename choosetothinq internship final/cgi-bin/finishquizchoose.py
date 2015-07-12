#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import urllib2
import base64					#built in python library for encoding decoding
from Crypto.Cipher import AES	# built in python library to get aes encryption
key=AES.new("choosetothinq321") #key used:- choosetothinq321
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
try:
	email=fs.getvalue("email")
	recv=base64.decodestring(email)
	email=key.decrypt(recv)			#decrypt the token to get email
	email=str(email).strip()
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	sql="SELECT `Score` FROM `game` WHERE `Email`='%s';"%(str(email))
	con.execute(sql)
	res=con.fetchone()
	score=int(res[0])
	sql1="SELECT `Total Score`,`No_of_games` FROM `register` WHERE `Email`='%s';"%(str(email))
	con.execute(sql1)
	res1=con.fetchone()
	ts=int(res1[0])+score	#total score
	nog=int(res1[1])+1	#no of games
	avgsscore=float(ts)/float(nog)	#avg score 
	sql2="UPDATE `register` SET `Total Score`='%d', `No_of_games`='%d', `Average Score`='%f' WHERE `Email`='%s';"%(int(ts),int(nog),float(avgsscore),str(email))			#update the total score,no of games and average score
	con.execute(sql2)
	db.commit()
	sql3="DELETE FROM `game` WHERE `Email`='%s';"%(str(email)) #delete the record from present playing players table i.e game table
	con.execute(sql3)
	db.commit()
	db.close()
	print score
except:
	pass
