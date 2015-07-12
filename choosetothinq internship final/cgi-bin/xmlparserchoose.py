def processxml(filequiz):
	from xml.dom import minidom #built in python library for xml parsing
	import MySQLdb
	import json
	from warnings import filterwarnings #built in python library to prevent printing of warnings
	filterwarnings('ignore', category = MySQLdb.Warning)
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	xmldoc=minidom.parse(filequiz) #parse xml file
	itemlist=xmldoc.getElementsByTagName('gameques')
	finalques=[]
	finalopt1=[]
	finalopt2=[]
	finalopt3=[]
	finalopt4=[]
	finalans=[]
	for i in itemlist:
		a=i.getElementsByTagName('question')[0]
		b=i.getElementsByTagName('option1')[0]
		c=i.getElementsByTagName('option2')[0]
		d=i.getElementsByTagName('option3')[0]
		e=i.getElementsByTagName('option4')[0]
		f=i.getElementsByTagName('answer')[0]
		finalques.append(str(a.childNodes[0].data))
		finalopt1.append(str(b.childNodes[0].data))
		finalopt2.append(str(c.childNodes[0].data))
		finalopt3.append(str(d.childNodes[0].data))
		finalopt4.append(str(e.childNodes[0].data))
		finalans.append(str(f.childNodes[0].data))
	try:
		sql="DROP TABLE IF EXISTS `questions`;"
		con.execute(sql)
		db.commit()
	except:
		pass
	sql1="CREATE TABLE `questions` (`question` varchar(999) NOT NULL,`option1` varchar(100) NOT NULL,`option2` varchar(100) NOT NULL,`option3` varchar(100) NOT NULL,`option4` varchar(100) NOT NULL,`correctans` varchar(100) NOT NULL,`id` int(100) NOT NULL AUTO_INCREMENT,`upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;"
	con.execute(sql1)
	db.commit()
	for dh in range(0,len(finalques)):
		finalques[dh]=MySQLdb.escape_string(finalques[dh])
		finalopt1[dh]=MySQLdb.escape_string(finalopt1[dh])
		finalopt2[dh]=MySQLdb.escape_string(finalopt2[dh])
		finalopt3[dh]=MySQLdb.escape_string(finalopt3[dh])
		finalopt4[dh]=MySQLdb.escape_string(finalopt4[dh])
		finalans[dh]=MySQLdb.escape_string(finalans[dh])
		sql1="INSERT INTO `questions`(`question`,`option1`,`option2`,`option3`,`option4`,`correctans`,`id`) VALUES('%s','%s','%s','%s','%s','%s','%d');"%(str(finalques[dh]),str(finalopt1[dh]),str(finalopt2[dh]),str(finalopt3[dh]),str(finalopt4[dh]),str(finalans[dh]),int(dh+1))
		con.execute(sql1)
		db.commit()
	ans=json.dumps({"valid":[{"answer":"**Your file has been successfully uploaded"}]})
	db.close()
	return ans
