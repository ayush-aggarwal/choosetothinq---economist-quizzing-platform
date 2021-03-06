-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 30, 2015 at 06:17 PM
-- Server version: 5.5.43-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `choosetothinq`
--
CREATE DATABASE IF NOT EXISTS `choosetothinq` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `choosetothinq`;

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--
-- Creation: Jun 11, 2015 at 04:36 PM
--

DROP TABLE IF EXISTS `feedback`;
CREATE TABLE IF NOT EXISTS `feedback` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `Name` varchar(9999) NOT NULL,
  `Email` varchar(9999) NOT NULL,
  `Message` varchar(9999) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22 ;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `Name`, `Email`, `Message`) VALUES
(1, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'Test Message'),
(2, 'Rishav Medhi', 'rishav164@gmail.com', 'test123'),
(3, 'Tilak Patidar', 'tilakpatidar@gmail.com', 'okok'),
(11, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'd3j32d2hfjh'),
(12, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'hjhjhjhjh'),
(13, 'Sagar Sahni', 'hello.sagarsahni@gmail.com', 'hjefjefjwefjwjehfjw'),
(14, 'Piyush Garg', 'piyush.garg@gmail.com', 'grtgetewt4w'),
(15, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'hggygygguiug'),
(16, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'kfhjjfjhfjwj'),
(17, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'jhjfhajfj'),
(18, 'Piyush Garg', 'piyush.garg@gmail.com', 'tough'),
(19, 'Piyush Garg', 'piyush.garg@gmail.com', 'very tough questions'),
(20, 'TEST21', 'test21@test21.com', 'test21'),
(21, 'Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'ok');

-- --------------------------------------------------------

--
-- Table structure for table `forgetpasswordrequest`
--
-- Creation: Jun 30, 2015 at 12:25 PM
--

DROP TABLE IF EXISTS `forgetpasswordrequest`;
CREATE TABLE IF NOT EXISTS `forgetpasswordrequest` (
  `Email` varchar(767) NOT NULL,
  `Password` varchar(999) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `forgetpasswordrequest`
--

INSERT INTO `forgetpasswordrequest` (`Email`, `Password`) VALUES
('ayush.agarwal7689@gmail.com', 'helloayush');

-- --------------------------------------------------------

--
-- Table structure for table `game`
--
-- Creation: May 28, 2015 at 03:16 PM
--

DROP TABLE IF EXISTS `game`;
CREATE TABLE IF NOT EXISTS `game` (
  `Name` varchar(300) NOT NULL,
  `Email` varchar(767) NOT NULL,
  `Score` int(255) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `game`
--

INSERT INTO `game` (`Name`, `Email`, `Score`) VALUES
('admini', 'admin@ghsh.jhfje', 0);

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--
-- Creation: Jun 28, 2015 at 02:01 PM
--

DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `question` varchar(999) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `correctans` varchar(100) NOT NULL,
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`question`, `option1`, `option2`, `option3`, `option4`, `correctans`, `id`, `upload_date`) VALUES
('South Korea and Japan marked the ___ anniversary of their diplomatic ties, which have been strained recently by South Korea''s misgivings about Japan''s attitude towards its role in the second world war.', '50th', '40th', '60th', '70th', '50th', 1, '2015-06-28 14:01:55'),
('2.	A recent surge of asylum seekers led ______ to say it would suspend its application of rules obliging people to apply for asylum in the first European Union country they reach.', 'France', 'Cyprus', 'Hungary', 'Italy', 'Hungary', 2, '2015-06-28 14:01:56'),
('The boss of Boeing, Jim McNerney is stepping down. _________, the planemaker''s chief operating officer, is to take the yoke.', 'Linda Cook', 'Dennis Muilenburg', 'James Bell', 'Lewis Platt', 'Dennis Muilenburg', 3, '2015-06-28 14:01:56'),
('The computer giant, Apple, have made a U-turn after initially saying they would not pay royalties to artists whose songs were played during a free trial period in their new music-streaming service.  This has now changed since ___________ "an American superstar" threatened to withdraw her new album.', 'Taylor Swift', 'Beyonce', 'Nicki Minaj', 'Miley Cyrus', 'Taylor Swift', 4, '2015-06-28 14:01:57'),
('Two huge European supermarket owners, ________________, have agreed to merge in a deal worth billions.', 'Aldi and Auchan', 'Cora and Lidl', 'SPAR and Ahold', 'Ahold and Delhaize', 'Ahold and Delhaize', 5, '2015-06-28 14:01:58'),
('________, a French telecoms firm, rejected a takeover offer worth billions from Altice, a competitor. A successful bid would have created France''s largest mobile operator.', 'Orange S.A.', 'Bouygues', 'Free', 'SFR', 'Bouygues', 6, '2015-06-28 14:01:59'),
('Dzhokhar Tsarnaev, the 21-year-old Boston marathon bomber has been ________ at a federal hearing held on June 24th.', 'given a life sentence', 'given 35 years to life in prison', 'sentenced to death', 'given a life sentence without parole', 'sentenced to death', 7, '2015-06-28 14:02:00'),
('Tidal a "music-streaming" service owned by Jay-Z lost its second boss in two months when _______ stepped down.', 'Peter Tonstad', 'Kanye West', 'Andy Chen', 'Madonna', 'Peter Tonstad', 8, '2015-06-28 14:02:03'),
('A Qatari investment fund joined forces with _________, the owner of the Miami Dolphins American football team, to bid for control of Formula 1.', 'Wayne Huizenga', 'Tom Garfinkel', 'Stephen Ross', 'Dennis Hickey', 'Stephen Ross', 9, '2015-06-28 14:02:06');

-- --------------------------------------------------------

--
-- Table structure for table `questions1`
--
-- Creation: Jun 09, 2015 at 06:41 AM
--

DROP TABLE IF EXISTS `questions1`;
CREATE TABLE IF NOT EXISTS `questions1` (
  `question` varchar(999) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `correctans` varchar(100) NOT NULL,
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=10 ;

--
-- Dumping data for table `questions1`
--

INSERT INTO `questions1` (`question`, `option1`, `option2`, `option3`, `option4`, `correctans`, `id`, `upload_date`) VALUES
('The Twitter campaign #unitedfortahera was mounted in support of a Muslim passenger on a United Airlines flight whose request for ______ was denied due to company guidelines aimed at deterring terrorism.', 'a USB cable', 'an in-flight seat change', 'an unopened can of soda', 'a metal knife', 'an unopened can of soda', 1, '2015-06-10 04:34:16'),
('Republican presidential candidates are rejecting ______, American education standards introduced in 2010 to set national benchmarks for the skills students should have by certain grades. Forty five states and the District of Columbia have adopted the standards.', 'Head Start', 'No Child Left Behind', 'the Common Core', 'the Montessori method', 'the Common Core', 2, '2015-06-10 04:34:17'),
('After 17 years, the president of FIFA, football''s governing body, resigned amid allegations of corruption. _____ had just won re-election on May 29th.', 'Chuck Blazer', 'Jack Warner', 'Jerome Valcke', 'Sepp Blatter', 'Sepp Blatter', 3, '2015-06-10 04:34:18'),
('The Italian city of ____ hosted its tenth annual celebration of economics. Nobel-prize-winner Joseph Stiglitz and Thomas Piketty, author of "Capital in the Twenty-First Century", were speakers this year.', 'Taranto', 'Tivoli', 'Trento', 'Turin', 'Trento', 4, '2015-06-10 04:34:19'),
('After years of cost-cutting under its old owners, ____ is experiencing a period of expansion under Jeff Bezos who bought the paper in 2013. Insiders are banking on Amazon bundling the paper into its Prime subscription.', 'The Boston Globe', 'Chicago Tribune', 'Los Angeles Times', 'The Washington Post', 'The Washington Post', 5, '2015-06-10 04:34:20'),
('Just ahead of mid-term elections scheduled for June 7th, the Mexican government backtracked on a constitutional reform approved by Congress in 2013 mandating _____.', 'examinations of teachers', 'oil-sector liberalisation', 'term limits for senators', 'taxes on junk food and sugary drinks', 'examinations of teachers', 6, '2015-06-10 04:34:21'),
('Following two disasters in 2014, _____ is now "technically" bankrupt, according to Christoph Mueller, its new boss.', 'AirAsia', 'Malaysia Airlines', 'Singapore Airlines', 'TransAsia Airways', 'Malaysia Airlines', 7, '2015-06-10 04:34:22'),
('The African Development Bank (AfDB), the biggest financier of infrastructure in Africa, appointed _____ as its new president.', 'Cape Verde''s Cristina Duarte', 'Nigeria''s Akinwumi Adesina', 'Rwanda''s Donald Kaberuka', 'Zimbabwe''s Thomas Sakala', 'Nigeria''s Akinwumi Adesina', 8, '2015-06-10 04:34:23'),
('When _____ amended its adoption law in 2012, it was intended to reduce unregistered adoptions of children overseas. But the law, which requires that births be registered with the government, has led to an increase in abandoned babies.', 'China', 'Romania', 'Russia', 'South Korea', 'South Korea', 9, '2015-06-10 04:34:24');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--
-- Creation: Jun 30, 2015 at 11:20 AM
--

DROP TABLE IF EXISTS `register`;
CREATE TABLE IF NOT EXISTS `register` (
  `Full Name` varchar(999) NOT NULL,
  `Email` varchar(767) NOT NULL,
  `Password` varchar(9999) NOT NULL,
  `Country` varchar(9999) NOT NULL,
  `Total Score` bigint(255) NOT NULL,
  `No_of_games` bigint(255) NOT NULL,
  `Average Score` float(65,0) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`Full Name`, `Email`, `Password`, `Country`, `Total Score`, `No_of_games`, `Average Score`) VALUES
('Ayush Aggarwal', 'ayush.agarwal7689@gmail.com', 'ayush12345', 'India', 40, 1, 40);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
