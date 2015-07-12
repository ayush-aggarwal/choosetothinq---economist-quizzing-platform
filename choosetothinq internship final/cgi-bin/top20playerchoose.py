#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
sql="SELECT `Full Name`,`Total Score`,`No_of_games`,`Average Score`,`Country` FROM `register` ORDER BY `Average Score` DESC LIMIT 20;"#get top 20 player with thier details
con.execute(sql)
res=con.fetchall()
i=1
final=[]
for r in res:
	r=list(r)
	r[1]=int(r[1])
	r[2]=int(r[2])
	r[3]=float(r[3])
	r.insert(0,i)	#insert rank
	i=i+1
	final.append(r)
ans=json.dumps({"top20":final})
print ans
db.close()
