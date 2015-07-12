def crawleco():	
	import MySQLdb
	import json
	import urllib2
	import economistcrawl1					#crawler for correct answer
	import os
	from warnings import filterwarnings
	filterwarnings('ignore', category = MySQLdb.Warning)	#avoid MySQLdb warnings to print
	final=[]
	morefinal=[]
	db=MySQLdb.connect("localhost","root","1","choosetothinq")# connection to mysql with root as username and 1 as password and database choosetothinq
	con=db.cursor()
	sql="DROP TABLE IF EXISTS `questions`;"
	con.execute(sql)
	db.commit()
	sql1="CREATE TABLE `questions` (`question` varchar(999) NOT NULL,`option1` varchar(100) NOT NULL,`option2` varchar(100) NOT NULL,`option3` varchar(100) NOT NULL,`option4` varchar(100) NOT NULL,`correctans` varchar(100) NOT NULL,`id` int(100) NOT NULL AUTO_INCREMENT,`upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;"
	con.execute(sql1)
	db.commit()
	data=urllib2.urlopen("http://economistsquares.economist.com/Game/").read()
	data=data.split("qvals[0] = [];",1)
	data=data[1]
	data=data.split("for (y = 0;",1)
	data=data[0]
	data=str(data).lstrip().rstrip()
	l1=data.split("\n")
	for r in l1:
		hj=r.strip()
		for i in range(0,9):
			if str(hj)=='qvals['+str(i)+'] = [];':
				if i!=1:
					del final[0]
				morefinal.append(final)
				final=[]
				break
			hj=hj.replace('qvals['+str(i)+']["question"] = ("','').replace('");','').strip()
			hj=hj.replace('qvals['+str(i)+']["questionid"] = ("','').replace('");','').strip()
			hj=hj.replace('qvals['+str(i)+']["option1"] = ("','').replace('");','').strip()
			hj=hj.replace('qvals['+str(i)+']["option2"] = ("','').replace('");','').strip()
			hj=hj.replace('qvals['+str(i)+']["option3"] = ("','').replace('");','').strip()
			hj=hj.replace('qvals['+str(i)+']["option4"] = ("','').replace('");','').strip()
		final.append(hj)
	del final[0]
	morefinal.append(final)
	v=1
	for a in morefinal:
		temp=a[0]
		a[0]=int(a[1])
		a[1]=temp
		cor=economistcrawl1.findcorrect(a[0])		#call findcorrect function to get correct option
		if str(cor)=="opt1":
			cor=str(a[2])
		elif str(cor)=="opt2":
			cor=str(a[3])
		elif str(cor)=="opt3":
			cor=str(a[4])
		elif str(cor)=="opt4":
			cor=str(a[5])
		a.append(cor)
		a.append(v)
		v=v+1
		del a[0]
		a=tuple(a)
		sql="INSERT INTO `questions` (`question`,`option1`,`option2`,`option3`,`option4`,`correctans`,`id`) VALUES('%s','%s','%s','%s','%s','%s','%d');"%a
		con.execute(sql)
		db.commit()
	db.close()
	os.remove('ques.xml')					#remove ques.xml on success crawling 
	ans=json.dumps({"valid":[{"answer":"**Data successfully Crawled!!"}]})
	return ans								
