#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import economistcrawl				#crawler made and imported
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
password=fs.getvalue("password")			#check password
if str(password)=="admin12345":
	ans=economistcrawl.crawleco()			#call crawleco function from econmoistcrawl.py
else:
	ans=json.dumps({"invalid":[{"answer":"**Incorrect Password!! Please Try Again"}]})
print ans
