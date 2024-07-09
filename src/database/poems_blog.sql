/*!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: poem_blog
-- ------------------------------------------------------
-- Server version	10.11.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author_id` int(11) NOT NULL,
  `poem_id` int(11) NOT NULL,
  `date_created` datetime NOT NULL DEFAULT current_timestamp(),
  `content` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `poem_id` (`poem_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`poem_id`) REFERENCES `poem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES
(1,1,1,'2024-07-09 16:18:11','Beautiful imagery in this poem.'),
(2,2,1,'2024-07-09 16:18:11','I love the way you describe the dawn.'),
(3,3,2,'2024-07-09 16:18:11','The nightfall description is so vivid.'),
(4,4,2,'2024-07-09 16:18:11','This poem captures the essence of night perfectly.'),
(5,5,3,'2024-07-09 16:18:11','Love eternal is beautifully written.'),
(6,6,3,'2024-07-09 16:18:11','The emotions in this poem are so raw.'),
(7,7,4,'2024-07-09 16:18:11','Winter\'s chill is a haunting poem.'),
(8,8,4,'2024-07-09 16:18:11','I can feel the cold in your words.'),
(9,9,5,'2024-07-09 16:18:11','Summer days are captured wonderfully.'),
(10,10,5,'2024-07-09 16:18:11','This poem makes me miss summer.'),
(11,1,6,'2024-07-09 16:18:11','Autumn leaves falling, so poetic.'),
(12,2,6,'2024-07-09 16:18:11','I love the imagery of autumn.'),
(13,3,7,'2024-07-09 16:18:11','Spring bloom is a refreshing read.'),
(14,4,7,'2024-07-09 16:18:11','Your words bring spring to life.'),
(15,5,8,'2024-07-09 16:18:11','Heartache is so relatable.'),
(16,6,8,'2024-07-09 16:18:11','This poem touched my heart.'),
(17,7,9,'2024-07-09 16:18:11','Joyful moments are well described.'),
(18,8,9,'2024-07-09 16:18:11','This poem made me smile.'),
(19,9,10,'2024-07-09 16:18:11','Silent tears, so profound.'),
(20,10,10,'2024-07-09 16:18:11','Your poem speaks to the soul.'),
(21,1,11,'2024-07-09 16:18:11','The storm is fierce in your words.'),
(22,2,11,'2024-07-09 16:18:11','I can hear the storm in your poem.'),
(23,3,12,'2024-07-09 16:18:11','Calm waters, beautifully written.'),
(24,4,12,'2024-07-09 16:18:11','Your poem brings peace.'),
(25,5,13,'2024-07-09 16:18:11','Mountain peak, what a view.'),
(26,6,13,'2024-07-09 16:18:11','Your words take me to the mountains.'),
(27,7,14,'2024-07-09 16:18:11','Forest whisper, so mysterious.'),
(28,8,14,'2024-07-09 16:18:11','I can hear the forest in your poem.'),
(29,9,15,'2024-07-09 16:18:11','City lights, wonderfully captured.'),
(30,10,15,'2024-07-09 16:18:11','Your poem brings the city to life.'),
(31,1,2,'2024-07-09 18:52:29','A thought-provoking poem about dreams'),
(32,1,2,'2024-07-09 19:46:00','A thought-provoking poem about dreams');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `followers`
--

DROP TABLE IF EXISTS `followers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `followers` (
  `follower_id` int(11) NOT NULL,
  `followed_id` int(11) NOT NULL,
  PRIMARY KEY (`follower_id`,`followed_id`),
  KEY `followed_id` (`followed_id`),
  CONSTRAINT `followers_ibfk_1` FOREIGN KEY (`follower_id`) REFERENCES `user` (`id`),
  CONSTRAINT `followers_ibfk_2` FOREIGN KEY (`followed_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `followers`
--

LOCK TABLES `followers` WRITE;
/*!40000 ALTER TABLE `followers` DISABLE KEYS */;
INSERT INTO `followers` VALUES
(1,2),
(1,3),
(1,4),
(2,1),
(2,3),
(2,4),
(2,5),
(3,1),
(3,2),
(3,4),
(3,6),
(4,1),
(4,2),
(4,3),
(4,5),
(5,1),
(5,2),
(5,3),
(6,1),
(6,2),
(6,3),
(7,1),
(7,2),
(7,3),
(8,1),
(8,2),
(8,3),
(9,1),
(9,2),
(9,3),
(10,1),
(10,2),
(10,3);
/*!40000 ALTER TABLE `followers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `poem_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`,`poem_id`),
  KEY `poem_id` (`poem_id`),
  CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`poem_id`) REFERENCES `poem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES
(1,1),
(1,5),
(1,10),
(2,1),
(2,6),
(2,11),
(3,1),
(3,6),
(3,11),
(4,2),
(4,7),
(4,12),
(5,2),
(5,7),
(5,12),
(6,3),
(6,8),
(6,13),
(7,3),
(7,8),
(7,13),
(8,4),
(8,9),
(8,14),
(9,4),
(9,9),
(9,14),
(10,5),
(10,10),
(10,15);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `poem`
--

DROP TABLE IF EXISTS `poem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `poem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `author_id` int(11) NOT NULL,
  `genre` varchar(50) NOT NULL,
  `date_created` datetime NOT NULL DEFAULT current_timestamp(),
  `description` varchar(255) DEFAULT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `poem_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poem`
--

LOCK TABLES `poem` WRITE;
/*!40000 ALTER TABLE `poem` DISABLE KEYS */;
INSERT INTO `poem` VALUES
(1,'The Dawn',1,'Nature','2024-07-09 16:15:49','A poem about the dawn','At the break of dawn, the world awakens...'),
(2,'Nightfall',2,'Nature','2024-07-09 16:15:49','A poem about the night','As the night falls, shadows grow...'),
(3,'Love Eternal',3,'Romance','2024-07-09 16:15:49','A poem about eternal love','Love eternal, forever in our hearts...'),
(4,'Winter\'s Chill',4,'Nature','2024-07-09 16:15:49','A poem about winter','The winter chill bites at my skin...'),
(5,'Summer Days',5,'Nature','2024-07-09 16:15:49','A poem about summer','Summer days, warm and bright...'),
(6,'Autumn Leaves',6,'Nature','2024-07-09 16:15:49','A poem about autumn','Autumn leaves fall gently to the ground...'),
(7,'Spring Bloom',7,'Nature','2024-07-09 16:15:49','A poem about spring','Spring blooms bring new life...'),
(8,'Heartache',8,'Romance','2024-07-09 16:15:49','A poem about heartache','Heartache follows love lost...'),
(9,'Joyful Moments',9,'Life','2024-07-09 16:15:49','A poem about joyful moments','Joyful moments we cherish forever...'),
(10,'Silent Tears',10,'Life','2024-07-09 16:15:49','A poem about silent tears','Silent tears fall in the night...'),
(11,'The Storm',1,'Nature','2024-07-09 16:15:49','A poem about a storm','The storm rages on, fierce and wild...'),
(12,'Calm Waters',2,'Nature','2024-07-09 16:15:49','A poem about calm waters','Calm waters reflect the sky above...'),
(13,'Mountain Peak',3,'Nature','2024-07-09 16:15:49','A poem about a mountain peak','From the mountain peak, the view is clear...'),
(14,'Forest Whisper',4,'Nature','2024-07-09 16:15:49','A poem about the forest','The forest whispers secrets untold...'),
(15,'City Lights',5,'Life','2024-07-09 16:15:49','A poem about city lights','City lights illuminate the night...'),
(16,'Desert Sands',6,'Nature','2024-07-09 16:15:49','A poem about the desert','Desert sands stretch endlessly...'),
(17,'Ocean Waves',7,'Nature','2024-07-09 16:15:49','A poem about the ocean','Ocean waves crash upon the shore...'),
(18,'Meadow Flowers',8,'Nature','2024-07-09 16:15:49','A poem about meadow flowers','Meadow flowers bloom in the sun...'),
(19,'Lonely Nights',9,'Life','2024-07-09 16:15:49','A poem about lonely nights','Lonely nights are quiet and cold...'),
(20,'Morning Dew',10,'Nature','2024-07-09 16:15:49','A poem about morning dew','Morning dew glistens on the grass...'),
(21,'Wandering Soul',1,'Life','2024-07-09 16:15:49','A poem about a wandering soul','A wandering soul seeks its path...'),
(22,'Echoes of Time',2,'Life','2024-07-09 16:15:49','A poem about time','Echoes of time linger in the air...'),
(23,'Forgotten Dreams',3,'Life','2024-07-09 16:15:49','A poem about forgotten dreams','Forgotten dreams fade away...'),
(24,'Burning Passion',4,'Romance','2024-07-09 16:15:49','A poem about passion','Burning passion ignites our hearts...'),
(25,'First Snow',5,'Nature','2024-07-09 16:15:49','A poem about the first snow','The first snow falls gently...'),
(26,'Rainy Days',6,'Nature','2024-07-09 16:15:49','A poem about rainy days','Rainy days bring a sense of peace...'),
(27,'Starry Night',7,'Nature','2024-07-09 16:15:49','A poem about a starry night','A starry night lights up the sky...'),
(28,'Whispering Winds',8,'Nature','2024-07-09 16:15:49','A poem about the wind','Whispering winds carry tales...'),
(29,'Golden Sunset',9,'Nature','2024-07-09 16:15:49','A poem about a sunset','A golden sunset marks the end...'),
(30,'Eternal Hope',10,'Life','2024-07-09 16:15:49','A poem about hope','Eternal hope keeps us moving forward...'),
(31,'Oda a la soledad',1,'Poesía lírica','2024-07-09 17:15:29','Reflexión sobre la soledad humana','En la quietud de la noche, el alma se encuentra consigo misma...');
/*!40000 ALTER TABLE `poem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(10) NOT NULL,
  `lastname` varchar(15) NOT NULL,
  `username` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `description` varchar(100) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'John','Doe','johndoe1','Male','A sample user','john.doe1@example.com','password1'),
(2,'Jane','Smith','janesmith1','Female','Another sample user','jane.smith1@example.com','password2'),
(3,'Mike','Johnson','mikejohnson1','Male','Yet another sample user','mike.johnson1@example.com','password3'),
(4,'Emily','Davis','emilydavis1','Female','Sample user number four','emily.davis1@example.com','password4'),
(5,'David','Wilson','davidwilson1','Male','Fifth sample user','david.wilson1@example.com','password5'),
(6,'Sarah','Miller','sarahmiller1','Female','Sixth sample user','sarah.miller1@example.com','password6'),
(7,'Robert','Brown','robertbrown1','Male','Seventh sample user','robert.brown1@example.com','password7'),
(8,'Linda','Jones','lindajones1','Female','Eighth sample user','linda.jones1@example.com','password8'),
(9,'James','Garcia','jamesgarcia1','Male','Ninth sample user','james.garcia1@example.com','password9'),
(10,'Laura','Martinez','lauramartinez1','Female','Tenth sample user','laura.martinez1@example.com','password10'),
(11,'John','Jaan','john_jaan','male','Lover of poetry and literature.','john.doe@example.com','hashedpassword123');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-09 19:48:34
