def processtxt(filename):	
	import MySQLdb
	import json
	from warnings import filterwarnings
	filterwarnings('ignore', category = MySQLdb.Warning)
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	try:
		sql="DROP TABLE IF EXISTS `questions`;"
		con.execute(sql)
		db.commit()
	except:
		pass
	sql1="CREATE TABLE `questions` (`question` varchar(999) NOT NULL,`option1` varchar(100) NOT NULL,`option2` varchar(100) NOT NULL,`option3` varchar(100) NOT NULL,`option4` varchar(100) NOT NULL,`correctans` varchar(100) NOT NULL,`id` int(100) NOT NULL AUTO_INCREMENT,`upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;"
	con.execute(sql1)
	db.commit()
	f=open(filename,"r")# open .txt file
	data=f.readlines()
	lifinal=[]
	v=1
	for i in range(0,len(data)):
		if str(data[i][0])!="\n":
			data[i]=MySQLdb.escape_string(str(data[i]).strip().replace("answer:- ",""))
			lifinal.append(data[i])
		else:
			lifinal.append(v)
			v=v+1
			lifinal=tuple(lifinal)
			sql="INSERT INTO `questions` (`question`,`option1`,`option2`,`option3`,`option4`,`correctans`,`id`) VALUES ('%s','%s','%s','%s','%s','%s','%d');"%lifinal
			con.execute(sql)
			db.commit()
			lifinal=[]
	lifinal.append(v)
	v=v+1
	lifinal=tuple(lifinal)
	sql="INSERT INTO `questions` (`question`,`option1`,`option2`,`option3`,`option4`,`correctans`,`id`) VALUES ('%s','%s','%s','%s','%s','%s','%d');"%lifinal
	con.execute(sql)
	db.commit()
	db.close()
	ans=json.dumps({"valid":[{"answer":"**Your file has been successfully uploaded"}]})
	return ans
