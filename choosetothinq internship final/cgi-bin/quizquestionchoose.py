#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
id1=fs.getvalue("id")
db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
con=db.cursor()
sql="SELECT * FROM `questions` WHERE `id`='%d';"%(int(id1)) # get question with id
con.execute(sql)
res=con.fetchone()
ques=str(res[0])	#get question
opt1=str(res[1])	#get option 1
opt2=str(res[2])	#get option 2
opt3=str(res[3])	#get option 3
opt4=str(res[4])	#get option 4
date=str(res[7])	#get date
date=date[0:date.index(" ")]	#get date in specific format
var=date.split("-")
dat=str(var[2])
year=str(var[0])
day=str(var[1])
if day=="01":
	day="January"
elif day=="02":
	day="Febuary"
elif day=="03":
	day="March"
elif day=="04":
	day="April"
elif day=="05":
	day="May"
elif day=="06":
	day="June"
elif day=="07":
	day="July"
elif day=="08":
	day="August"
elif day=="09":
	day="September"
elif day=="10":
	day="October"
elif day=="11":
	day="November"
elif day=="12":
	day="December"
ans=json.dumps({"valid":[{"date":"Questions from "+str(day)+" "+str(dat)+","+str(year),"question":ques,"opt1":opt1,"opt2":opt2,"opt3":opt3,"opt4":opt4}]})
db.close()
print ans

