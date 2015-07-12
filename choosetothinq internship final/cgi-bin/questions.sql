-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: choosetothinq
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `question` varchar(999) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `correctans` varchar(100) NOT NULL,
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES ('The Twitter campaign #unitedfortahera was mounted in support of a Muslim passenger on a United Airlines flight whose request for ______ was denied due to company guidelines aimed at deterring terrorism.','a USB cable','an in-flight seat change','an unopened can of soda','a metal knife','an unopened can of soda',1,'2015-06-09 06:56:41'),('Republican presidential candidates are rejecting ______, American education standards introduced in 2010 to set national benchmarks for the skills students should have by certain grades. Forty five states and the District of Columbia have adopted the standards.','Head Start','No Child Left Behind','the Common Core','the Montessori method','the Common Core',2,'2015-06-09 06:56:41'),('After 17 years, the president of FIFA, football\'s governing body, resigned amid allegations of corruption. _____ had just won re-election on May 29th.','Chuck Blazer','Jack Warner','Jerome Valcke','Sepp Blatter','Sepp Blatter',3,'2015-06-09 06:56:41'),('The Italian city of ____ hosted its tenth annual celebration of economics. Nobel-prize-winner Joseph Stiglitz and Thomas Piketty, author of \"Capital in the Twenty-First Century\", were speakers this year.','Taranto','Tivoli','Trento','Turin','Trento',4,'2015-06-09 06:56:41'),('After years of cost-cutting under its old owners, ____ is experiencing a period of expansion under Jeff Bezos who bought the paper in 2013. Insiders are banking on Amazon bundling the paper into its Prime subscription.','The Boston Globe','Chicago Tribune','Los Angeles Times','The Washington Post','The Washington Post',5,'2015-06-09 06:56:41'),('Just ahead of mid-term elections scheduled for June 7th, the Mexican government backtracked on a constitutional reform approved by Congress in 2013 mandating _____.','examinations of teachers','oil-sector liberalisation','term limits for senators','taxes on junk food and sugary drinks','examinations of teachers',6,'2015-06-09 06:56:41'),('Following two disasters in 2014, _____ is now \"technically\" bankrupt, according to Christoph Mueller, its new boss.','AirAsia','Malaysia Airlines','Singapore Airlines','TransAsia Airways','Malaysia Airlines',7,'2015-06-09 06:56:41'),('The African Development Bank (AfDB), the biggest financier of infrastructure in Africa, appointed _____ as its new president.','Cape Verde\'s Cristina Duarte','Nigeria\'s Akinwumi Adesina','Rwanda\'s Donald Kaberuka','Zimbabwe\'s Thomas Sakala','Nigeria\'s Akinwumi Adesina',8,'2015-06-09 06:56:41'),('When _____ amended its adoption law in 2012, it was intended to reduce unregistered adoptions of children overseas. But the law, which requires that births be registered with the government, has led to an increase in abandoned babies.','China','Romania','Russia','South Korea','South Korea',9,'2015-06-09 06:56:41');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-09 12:29:26
