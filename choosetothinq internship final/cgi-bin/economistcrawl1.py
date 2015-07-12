def findcorrect(qid):
	import MySQLdb
	import urllib2
	from xml.dom import minidom
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	data=urllib2.urlopen("http://economistsquares.economist.com/HighTrafficAPI/?Action=GameSolveQuestion&QuestionID="+str(qid)+"&Guess=1").read()
	data=str(data).strip()
	f=open("ques.xml","w")	#store xml obtained in file so that minidom can work 
	f.write(data)
	f.close()
	xmldoc=minidom.parse("ques.xml")
	a=xmldoc.getElementsByTagName('CorrectAnswer')[0]
	option="opt"+str(a.childNodes[0].data)
	db.close()
	return option
