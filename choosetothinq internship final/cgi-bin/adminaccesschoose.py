#!/usr/bin/python -v3
import cgi,cgitb
import MySQLdb
import json
import sqlparse					# built in sqlparse python library
import xmlparserchoose			# made xmlparserchoose.py and imported
import txtparserchoose			# made txtparserchoose.py and imported
cgitb.enable()
print "Content-Type: text/html\n"
fs=cgi.FieldStorage()
password=fs.getvalue("password")		#take password
quizfile=fs.getvalue("quizfile")		#take path of the file
quizfile=str(quizfile).replace("C:\\fakepath\\","")
if str(password)=="admin12345":				#check if the password is admin12345 to verify the administrator
	if "." in quizfile:						#check if filename has an extension
		a=quizfile.rsplit(".",1)
		ext=str(a[1])
		if ext=="sql":						#for .sql files
			sql = open(quizfile).read()
			sql_parts = sqlparse.split(sql)			
			db=MySQLdb.connect("localhost","root","1","choosetothinq")	# connection to mysql with root as username and 1 as password and database choosetothinq
			con=db.cursor()
			for sql_part in sql_parts:
				if sql_part.strip()=='':
					continue
   				con.execute(sql_part)
			ans=json.dumps({"valid":[{"answer":"**Your file has been successfully uploaded"}]})
			db.close()
		elif ext=="xml":					#for .xml files
			ans=xmlparserchoose.processxml(quizfile)		
		elif ext=="txt":					#for .txt files
			ans=txtparserchoose.processtxt(quizfile)
		else:
			ans=json.dumps({"invalid":[{"answer":"**Please upload a .sql, .xml or .txt files !!"}]})
	else:
		ans=json.dumps({"invalid":[{"answer":"**Please upload a valid file"}]})
else:
	ans=json.dumps({"invalid":[{"answer":"**Incorrect Password!! Please Try Again"}]})
print ans
