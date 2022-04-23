DROP DATABASE IF EXISTS `binance`;
CREATE DATABASE  IF NOT EXISTS `binance` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `binance`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: binance
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `market`
--

DROP TABLE IF EXISTS `market`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `market` (
  `MarketID` int NOT NULL AUTO_INCREMENT,
  `Token1` varchar(50) NOT NULL,
  `Token2` varchar(50) NOT NULL,
  PRIMARY KEY (`MarketID`),
  UNIQUE KEY `MarketID` (`MarketID`),
  UNIQUE KEY `Token1` (`Token1`,`Token2`),
  CONSTRAINT `TokenOrder` CHECK ((`Token1` < `Token2`))
) ENGINE=InnoDB AUTO_INCREMENT=486 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `market`
--

LOCK TABLES `market` WRITE;
/*!40000 ALTER TABLE `market` DISABLE KEYS */;
INSERT INTO `market` VALUES (255,'Aave','Tether'),(446,'Aave','USD Coin'),(27,'Algorand','Bitcoin'),(318,'Algorand','BNB'),(125,'Algorand','Ethereum'),(222,'Algorand','Tether'),(413,'Algorand','USD Coin'),(90,'Amp','Bitcoin'),(381,'Amp','BNB'),(188,'Amp','Ethereum'),(285,'Amp','Tether'),(476,'Amp','USD Coin'),(54,'ApeCoin','Bitcoin'),(345,'ApeCoin','BNB'),(152,'ApeCoin','Ethereum'),(249,'ApeCoin','Tether'),(440,'ApeCoin','USD Coin'),(70,'Arweave','Bitcoin'),(361,'Arweave','BNB'),(168,'Arweave','Ethereum'),(265,'Arweave','Tether'),(456,'Arweave','USD Coin'),(10,'Avalanche','Bitcoin'),(301,'Avalanche','BNB'),(108,'Avalanche','Ethereum'),(205,'Avalanche','Tether'),(396,'Avalanche','USD Coin'),(32,'Axie Infinity','Bitcoin'),(323,'Axie Infinity','BNB'),(130,'Axie Infinity','Ethereum'),(227,'Axie Infinity','Tether'),(418,'Axie Infinity','USD Coin'),(87,'Basic Attention Token','Bitcoin'),(378,'Basic Attention Token','BNB'),(185,'Basic Attention Token','Ethereum'),(282,'Basic Attention Token','Tether'),(473,'Basic Attention Token','USD Coin'),(12,'Binance USD','Bitcoin'),(303,'Binance USD','BNB'),(110,'Binance USD','Ethereum'),(207,'Binance USD','Tether'),(398,'Binance USD','USD Coin'),(24,'Bitcoin','Bitcoin Cash'),(73,'Bitcoin','Bitcoin SV'),(98,'Bitcoin','BitDAO'),(66,'Bitcoin','BitTorrent'),(3,'Bitcoin','BNB'),(6,'Bitcoin','Cardano'),(62,'Bitcoin','cDAI'),(85,'Bitcoin','Celo'),(84,'Bitcoin','Celsius Network'),(44,'Bitcoin','cETH'),(23,'Bitcoin','Chainlink'),(83,'Bitcoin','Chiliz'),(75,'Bitcoin','Convex Finance'),(21,'Bitcoin','Cosmos Hub'),(16,'Bitcoin','Cronos'),(61,'Bitcoin','cUSDC'),(19,'Bitcoin','Dai'),(82,'Bitcoin','Dash'),(39,'Bitcoin','Decentraland'),(11,'Bitcoin','Dogecoin'),(72,'Bitcoin','eCash'),(37,'Bitcoin','Elrond'),(74,'Bitcoin','Enjin Coin'),(50,'Bitcoin','EOS'),(1,'Bitcoin','Ethereum'),(28,'Bitcoin','Ethereum Classic'),(43,'Bitcoin','Fantom'),(38,'Bitcoin','Filecoin'),(56,'Bitcoin','Flow'),(53,'Bitcoin','Frax'),(93,'Bitcoin','Frax Share'),(25,'Bitcoin','FTX Token'),(64,'Bitcoin','Gala'),(65,'Bitcoin','Harmony'),(35,'Bitcoin','Hedera'),(57,'Bitcoin','Helium'),(96,'Bitcoin','Holo'),(91,'Bitcoin','Humans.ai'),(71,'Bitcoin','Huobi BTC'),(86,'Bitcoin','Huobi Token'),(36,'Bitcoin','Internet Computer'),(58,'Bitcoin','IOTA'),(92,'Bitcoin','JUNO'),(95,'Bitcoin','Kadena'),(46,'Bitcoin','Klaytn'),(80,'Bitcoin','KuCoin Token'),(78,'Bitcoin','Kusama'),(31,'Bitcoin','LEO Token'),(18,'Bitcoin','Lido Staked Ether'),(20,'Bitcoin','Litecoin'),(81,'Bitcoin','Loopring'),(52,'Bitcoin','Magic Internet Money'),(67,'Bitcoin','Maker'),(97,'Bitcoin','Mina Protocol'),(41,'Bitcoin','Monero'),(22,'Bitcoin','Near'),(99,'Bitcoin','NEM'),(69,'Bitcoin','NEO'),(89,'Bitcoin','NEXO'),(29,'Bitcoin','OKB'),(51,'Bitcoin','Osmosis'),(59,'Bitcoin','PancakeSwap'),(9,'Bitcoin','Polkadot'),(17,'Bitcoin','Polygon'),(63,'Bitcoin','Quant'),(77,'Bitcoin','Radix'),(14,'Bitcoin','Shiba Inu'),(7,'Bitcoin','Solana'),(79,'Bitcoin','Stacks'),(30,'Bitcoin','Stellar'),(94,'Bitcoin','Synthetix Network Token'),(8,'Bitcoin','Terra'),(13,'Bitcoin','TerraUSD'),(2,'Bitcoin','Tether'),(45,'Bitcoin','Tezos'),(49,'Bitcoin','The Graph'),(40,'Bitcoin','The Sandbox'),(68,'Bitcoin','Theta Fuel'),(42,'Bitcoin','Theta Network'),(48,'Bitcoin','THORChain'),(26,'Bitcoin','TRON'),(88,'Bitcoin','TrueUSD'),(34,'Bitcoin','Uniswap'),(4,'Bitcoin','USD Coin'),(33,'Bitcoin','VeChain'),(47,'Bitcoin','Waves'),(15,'Bitcoin','Wrapped Bitcoin'),(5,'Bitcoin','XRP'),(55,'Bitcoin','Zcash'),(76,'Bitcoin','Zilliqa'),(315,'Bitcoin Cash','BNB'),(122,'Bitcoin Cash','Ethereum'),(219,'Bitcoin Cash','Tether'),(410,'Bitcoin Cash','USD Coin'),(364,'Bitcoin SV','BNB'),(171,'Bitcoin SV','Ethereum'),(268,'Bitcoin SV','Tether'),(459,'Bitcoin SV','USD Coin'),(389,'BitDAO','BNB'),(196,'BitDAO','Ethereum'),(293,'BitDAO','Tether'),(484,'BitDAO','USD Coin'),(357,'BitTorrent','BNB'),(164,'BitTorrent','Ethereum'),(261,'BitTorrent','Tether'),(452,'BitTorrent','USD Coin'),(297,'BNB','Cardano'),(353,'BNB','cDAI'),(376,'BNB','Celo'),(375,'BNB','Celsius Network'),(335,'BNB','cETH'),(314,'BNB','Chainlink'),(374,'BNB','Chiliz'),(366,'BNB','Convex Finance'),(312,'BNB','Cosmos Hub'),(307,'BNB','Cronos'),(352,'BNB','cUSDC'),(310,'BNB','Dai'),(373,'BNB','Dash'),(330,'BNB','Decentraland'),(302,'BNB','Dogecoin'),(363,'BNB','eCash'),(328,'BNB','Elrond'),(365,'BNB','Enjin Coin'),(341,'BNB','EOS'),(101,'BNB','Ethereum'),(319,'BNB','Ethereum Classic'),(334,'BNB','Fantom'),(329,'BNB','Filecoin'),(347,'BNB','Flow'),(344,'BNB','Frax'),(384,'BNB','Frax Share'),(316,'BNB','FTX Token'),(355,'BNB','Gala'),(356,'BNB','Harmony'),(326,'BNB','Hedera'),(348,'BNB','Helium'),(387,'BNB','Holo'),(382,'BNB','Humans.ai'),(362,'BNB','Huobi BTC'),(377,'BNB','Huobi Token'),(327,'BNB','Internet Computer'),(349,'BNB','IOTA'),(383,'BNB','JUNO'),(386,'BNB','Kadena'),(337,'BNB','Klaytn'),(371,'BNB','KuCoin Token'),(369,'BNB','Kusama'),(322,'BNB','LEO Token'),(309,'BNB','Lido Staked Ether'),(311,'BNB','Litecoin'),(372,'BNB','Loopring'),(343,'BNB','Magic Internet Money'),(358,'BNB','Maker'),(388,'BNB','Mina Protocol'),(332,'BNB','Monero'),(313,'BNB','Near'),(390,'BNB','NEM'),(360,'BNB','NEO'),(380,'BNB','NEXO'),(320,'BNB','OKB'),(342,'BNB','Osmosis'),(350,'BNB','PancakeSwap'),(300,'BNB','Polkadot'),(308,'BNB','Polygon'),(354,'BNB','Quant'),(368,'BNB','Radix'),(305,'BNB','Shiba Inu'),(298,'BNB','Solana'),(370,'BNB','Stacks'),(321,'BNB','Stellar'),(385,'BNB','Synthetix Network Token'),(299,'BNB','Terra'),(304,'BNB','TerraUSD'),(198,'BNB','Tether'),(336,'BNB','Tezos'),(340,'BNB','The Graph'),(331,'BNB','The Sandbox'),(359,'BNB','Theta Fuel'),(333,'BNB','Theta Network'),(339,'BNB','THORChain'),(317,'BNB','TRON'),(379,'BNB','TrueUSD'),(325,'BNB','Uniswap'),(295,'BNB','USD Coin'),(324,'BNB','VeChain'),(338,'BNB','Waves'),(306,'BNB','Wrapped Bitcoin'),(296,'BNB','XRP'),(346,'BNB','Zcash'),(367,'BNB','Zilliqa'),(104,'Cardano','Ethereum'),(201,'Cardano','Tether'),(392,'Cardano','USD Coin'),(160,'cDAI','Ethereum'),(257,'cDAI','Tether'),(448,'cDAI','USD Coin'),(183,'Celo','Ethereum'),(280,'Celo','Tether'),(471,'Celo','USD Coin'),(182,'Celsius Network','Ethereum'),(279,'Celsius Network','Tether'),(470,'Celsius Network','USD Coin'),(142,'cETH','Ethereum'),(239,'cETH','Tether'),(430,'cETH','USD Coin'),(121,'Chainlink','Ethereum'),(218,'Chainlink','Tether'),(409,'Chainlink','USD Coin'),(181,'Chiliz','Ethereum'),(278,'Chiliz','Tether'),(469,'Chiliz','USD Coin'),(173,'Convex Finance','Ethereum'),(270,'Convex Finance','Tether'),(461,'Convex Finance','USD Coin'),(119,'Cosmos Hub','Ethereum'),(216,'Cosmos Hub','Tether'),(407,'Cosmos Hub','USD Coin'),(114,'Cronos','Ethereum'),(211,'Cronos','Tether'),(402,'Cronos','USD Coin'),(159,'cUSDC','Ethereum'),(256,'cUSDC','Tether'),(447,'cUSDC','USD Coin'),(117,'Dai','Ethereum'),(214,'Dai','Tether'),(405,'Dai','USD Coin'),(180,'Dash','Ethereum'),(277,'Dash','Tether'),(468,'Dash','USD Coin'),(137,'Decentraland','Ethereum'),(234,'Decentraland','Tether'),(425,'Decentraland','USD Coin'),(109,'Dogecoin','Ethereum'),(206,'Dogecoin','Tether'),(397,'Dogecoin','USD Coin'),(170,'eCash','Ethereum'),(267,'eCash','Tether'),(458,'eCash','USD Coin'),(135,'Elrond','Ethereum'),(232,'Elrond','Tether'),(423,'Elrond','USD Coin'),(172,'Enjin Coin','Ethereum'),(269,'Enjin Coin','Tether'),(460,'Enjin Coin','USD Coin'),(148,'EOS','Ethereum'),(245,'EOS','Tether'),(436,'EOS','USD Coin'),(126,'Ethereum','Ethereum Classic'),(141,'Ethereum','Fantom'),(136,'Ethereum','Filecoin'),(154,'Ethereum','Flow'),(151,'Ethereum','Frax'),(191,'Ethereum','Frax Share'),(123,'Ethereum','FTX Token'),(162,'Ethereum','Gala'),(163,'Ethereum','Harmony'),(133,'Ethereum','Hedera'),(155,'Ethereum','Helium'),(194,'Ethereum','Holo'),(189,'Ethereum','Humans.ai'),(169,'Ethereum','Huobi BTC'),(184,'Ethereum','Huobi Token'),(134,'Ethereum','Internet Computer'),(156,'Ethereum','IOTA'),(190,'Ethereum','JUNO'),(193,'Ethereum','Kadena'),(144,'Ethereum','Klaytn'),(178,'Ethereum','KuCoin Token'),(176,'Ethereum','Kusama'),(129,'Ethereum','LEO Token'),(116,'Ethereum','Lido Staked Ether'),(118,'Ethereum','Litecoin'),(179,'Ethereum','Loopring'),(150,'Ethereum','Magic Internet Money'),(165,'Ethereum','Maker'),(195,'Ethereum','Mina Protocol'),(139,'Ethereum','Monero'),(120,'Ethereum','Near'),(197,'Ethereum','NEM'),(167,'Ethereum','NEO'),(187,'Ethereum','NEXO'),(127,'Ethereum','OKB'),(149,'Ethereum','Osmosis'),(157,'Ethereum','PancakeSwap'),(107,'Ethereum','Polkadot'),(115,'Ethereum','Polygon'),(161,'Ethereum','Quant'),(175,'Ethereum','Radix'),(112,'Ethereum','Shiba Inu'),(105,'Ethereum','Solana'),(177,'Ethereum','Stacks'),(128,'Ethereum','Stellar'),(192,'Ethereum','Synthetix Network Token'),(106,'Ethereum','Terra'),(111,'Ethereum','TerraUSD'),(100,'Ethereum','Tether'),(143,'Ethereum','Tezos'),(147,'Ethereum','The Graph'),(138,'Ethereum','The Sandbox'),(166,'Ethereum','Theta Fuel'),(140,'Ethereum','Theta Network'),(146,'Ethereum','THORChain'),(124,'Ethereum','TRON'),(186,'Ethereum','TrueUSD'),(132,'Ethereum','Uniswap'),(102,'Ethereum','USD Coin'),(131,'Ethereum','VeChain'),(145,'Ethereum','Waves'),(113,'Ethereum','Wrapped Bitcoin'),(103,'Ethereum','XRP'),(153,'Ethereum','Zcash'),(174,'Ethereum','Zilliqa'),(223,'Ethereum Classic','Tether'),(414,'Ethereum Classic','USD Coin'),(238,'Fantom','Tether'),(429,'Fantom','USD Coin'),(233,'Filecoin','Tether'),(424,'Filecoin','USD Coin'),(251,'Flow','Tether'),(442,'Flow','USD Coin'),(248,'Frax','Tether'),(439,'Frax','USD Coin'),(288,'Frax Share','Tether'),(479,'Frax Share','USD Coin'),(220,'FTX Token','Tether'),(411,'FTX Token','USD Coin'),(259,'Gala','Tether'),(450,'Gala','USD Coin'),(260,'Harmony','Tether'),(451,'Harmony','USD Coin'),(230,'Hedera','Tether'),(421,'Hedera','USD Coin'),(252,'Helium','Tether'),(443,'Helium','USD Coin'),(291,'Holo','Tether'),(482,'Holo','USD Coin'),(286,'Humans.ai','Tether'),(477,'Humans.ai','USD Coin'),(266,'Huobi BTC','Tether'),(457,'Huobi BTC','USD Coin'),(281,'Huobi Token','Tether'),(472,'Huobi Token','USD Coin'),(231,'Internet Computer','Tether'),(422,'Internet Computer','USD Coin'),(253,'IOTA','Tether'),(444,'IOTA','USD Coin'),(287,'JUNO','Tether'),(478,'JUNO','USD Coin'),(290,'Kadena','Tether'),(481,'Kadena','USD Coin'),(241,'Klaytn','Tether'),(432,'Klaytn','USD Coin'),(275,'KuCoin Token','Tether'),(466,'KuCoin Token','USD Coin'),(273,'Kusama','Tether'),(464,'Kusama','USD Coin'),(226,'LEO Token','Tether'),(417,'LEO Token','USD Coin'),(213,'Lido Staked Ether','Tether'),(404,'Lido Staked Ether','USD Coin'),(215,'Litecoin','Tether'),(406,'Litecoin','USD Coin'),(276,'Loopring','Tether'),(467,'Loopring','USD Coin'),(247,'Magic Internet Money','Tether'),(438,'Magic Internet Money','USD Coin'),(262,'Maker','Tether'),(453,'Maker','USD Coin'),(292,'Mina Protocol','Tether'),(483,'Mina Protocol','USD Coin'),(236,'Monero','Tether'),(427,'Monero','USD Coin'),(217,'Near','Tether'),(408,'Near','USD Coin'),(294,'NEM','Tether'),(485,'NEM','USD Coin'),(264,'NEO','Tether'),(455,'NEO','USD Coin'),(284,'NEXO','Tether'),(475,'NEXO','USD Coin'),(224,'OKB','Tether'),(415,'OKB','USD Coin'),(246,'Osmosis','Tether'),(437,'Osmosis','USD Coin'),(254,'PancakeSwap','Tether'),(445,'PancakeSwap','USD Coin'),(204,'Polkadot','Tether'),(395,'Polkadot','USD Coin'),(212,'Polygon','Tether'),(403,'Polygon','USD Coin'),(258,'Quant','Tether'),(449,'Quant','USD Coin'),(272,'Radix','Tether'),(463,'Radix','USD Coin'),(209,'Shiba Inu','Tether'),(400,'Shiba Inu','USD Coin'),(202,'Solana','Tether'),(393,'Solana','USD Coin'),(274,'Stacks','Tether'),(465,'Stacks','USD Coin'),(225,'Stellar','Tether'),(416,'Stellar','USD Coin'),(289,'Synthetix Network Token','Tether'),(480,'Synthetix Network Token','USD Coin'),(203,'Terra','Tether'),(394,'Terra','USD Coin'),(208,'TerraUSD','Tether'),(399,'TerraUSD','USD Coin'),(240,'Tether','Tezos'),(244,'Tether','The Graph'),(235,'Tether','The Sandbox'),(263,'Tether','Theta Fuel'),(237,'Tether','Theta Network'),(243,'Tether','THORChain'),(221,'Tether','TRON'),(283,'Tether','TrueUSD'),(229,'Tether','Uniswap'),(199,'Tether','USD Coin'),(228,'Tether','VeChain'),(242,'Tether','Waves'),(210,'Tether','Wrapped Bitcoin'),(200,'Tether','XRP'),(250,'Tether','Zcash'),(271,'Tether','Zilliqa'),(431,'Tezos','USD Coin'),(435,'The Graph','USD Coin'),(426,'The Sandbox','USD Coin'),(454,'Theta Fuel','USD Coin'),(428,'Theta Network','USD Coin'),(434,'THORChain','USD Coin'),(412,'TRON','USD Coin'),(474,'TrueUSD','USD Coin'),(420,'Uniswap','USD Coin'),(419,'USD Coin','VeChain'),(433,'USD Coin','Waves'),(401,'USD Coin','Wrapped Bitcoin'),(391,'USD Coin','XRP'),(441,'USD Coin','Zcash'),(462,'USD Coin','Zilliqa');
/*!40000 ALTER TABLE `market` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `markethistory`
--

DROP TABLE IF EXISTS `markethistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `markethistory` (
  `MarketHistoryID` int NOT NULL AUTO_INCREMENT,
  `MarketID` int NOT NULL,
  `Volume` double(30,10) NOT NULL,
  PRIMARY KEY (`MarketHistoryID`),
  KEY `fk_MarketHistory_Market` (`MarketID`),
  CONSTRAINT `fk_MarketHistory_Market` FOREIGN KEY (`MarketID`) REFERENCES `market` (`MarketID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `MarketVolumePositive` CHECK ((`Volume` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `markethistory`
--

LOCK TABLES `markethistory` WRITE;
/*!40000 ALTER TABLE `markethistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `markethistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marketorder`
--

DROP TABLE IF EXISTS `marketorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marketorder` (
  `MarketOrderID` int NOT NULL AUTO_INCREMENT,
  `UserName` varchar(50) NOT NULL,
  `MarketID` int NOT NULL,
  `OrderAction` enum('BUY','SELL') NOT NULL,
  `TotalAmount` double(30,10) NOT NULL,
  `RemainAmount` double(30,10) NOT NULL,
  `Price` double(30,10) NOT NULL,
  PRIMARY KEY (`MarketOrderID`),
  UNIQUE KEY `MarketOrderID` (`MarketOrderID`),
  KEY `fk_MarketOrder_User` (`UserName`),
  KEY `fk_MarketOrder_Market` (`MarketID`),
  CONSTRAINT `fk_MarketOrder_Market` FOREIGN KEY (`MarketID`) REFERENCES `market` (`MarketID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_MarketOrder_User` FOREIGN KEY (`UserName`) REFERENCES `user` (`UserName`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `PricePositive` CHECK ((`Price` > 0)),
  CONSTRAINT `RemainAmountPositive` CHECK ((`RemainAmount` >= 0)),
  CONSTRAINT `TotalAmountConstraint` CHECK ((`TotalAmount` >= `RemainAmount`))
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marketorder`
--

LOCK TABLES `marketorder` WRITE;
/*!40000 ALTER TABLE `marketorder` DISABLE KEYS */;
INSERT INTO `marketorder` VALUES (51,'hien',8,'SELL',5.0000000000,0.0000000000,20.0000000000),(52,'hien',8,'SELL',5.0000000000,0.0000000000,20.0000000000),(53,'hien',8,'SELL',5.0000000000,0.0000000000,20.0000000000),(54,'ming',8,'SELL',10.0000000000,5.0000000000,50.0000000000),(55,'ming',8,'SELL',15.0000000000,15.0000000000,60.0000000000),(56,'duyen',8,'BUY',20.0000000000,0.0000000000,100.0000000000);
/*!40000 ALTER TABLE `marketorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderhistory`
--

DROP TABLE IF EXISTS `orderhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderhistory` (
  `OrderHistoryID` int NOT NULL AUTO_INCREMENT,
  `MarketOrderID` int NOT NULL,
  `Amount` double(30,10) NOT NULL,
  `OrderedAt` datetime NOT NULL,
  PRIMARY KEY (`OrderHistoryID`),
  KEY `fk_OrderHistory_MarketOrder` (`MarketOrderID`),
  CONSTRAINT `fk_OrderHistory_MarketOrder` FOREIGN KEY (`MarketOrderID`) REFERENCES `marketorder` (`MarketOrderID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `AmountOrderHistory` CHECK ((`Amount` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderhistory`
--

LOCK TABLES `orderhistory` WRITE;
/*!40000 ALTER TABLE `orderhistory` DISABLE KEYS */;
INSERT INTO `orderhistory` VALUES (164,56,5.0000000000,'2022-04-23 16:03:48'),(165,51,5.0000000000,'2022-04-23 16:03:48'),(166,56,5.0000000000,'2022-04-23 16:03:48'),(167,52,5.0000000000,'2022-04-23 16:03:48'),(168,56,5.0000000000,'2022-04-23 16:03:49'),(169,53,5.0000000000,'2022-04-23 16:03:49'),(170,56,5.0000000000,'2022-04-23 16:03:49'),(171,54,5.0000000000,'2022-04-23 16:03:49');
/*!40000 ALTER TABLE `orderhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token` (
  `TokenName` varchar(50) NOT NULL,
  `TokenSymbol` varchar(10) NOT NULL,
  `TokenImage` varchar(1000) DEFAULT NULL,
  `MarketCap` double(30,10) NOT NULL,
  `TotalSupply` double(30,10) NOT NULL,
  `MaxSupply` double(30,10) NOT NULL,
  `CoingeckoPrice` double(30,10) NOT NULL,
  PRIMARY KEY (`TokenName`),
  UNIQUE KEY `TokenName` (`TokenName`),
  UNIQUE KEY `TokenSymbol` (`TokenSymbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token`
--

LOCK TABLES `token` WRITE;
/*!40000 ALTER TABLE `token` DISABLE KEYS */;
INSERT INTO `token` VALUES ('Aave','aave','https://assets.coingecko.com/coins/images/12645/large/AAVE.png?1601374110',2336610781.0000000000,16000000.0000000000,16000000.0000000000,171.0100000000),('Algorand','algo','https://assets.coingecko.com/coins/images/4380/large/download.png?1547039725',6380791179.0000000000,7068124403.1374100000,10000000000.0000000000,0.9623740000),('Amp','amp','https://assets.coingecko.com/coins/images/12409/large/amp-200x200.png?1599625397',1329502899.0000000000,99443796846.1635000000,99225164238.5015300000,0.0277319400),('ApeCoin','ape','https://assets.coingecko.com/coins/images/24383/large/apecoin.jpg?1647476455',2543198972.0000000000,1000000000.0000000000,1000000000.0000000000,15.0100000000),('Arweave','ar','https://assets.coingecko.com/coins/images/4343/large/oRt6SiEN_400x400.jpg?1591059616',1877821695.0000000000,64598643.0000000000,66000000.0000000000,37.4800000000),('Avalanche','avax','https://assets.coingecko.com/coins/images/12559/large/coin-round-red.png?1604021818',24285600714.0000000000,377752194.4695483000,720000000.0000000000,90.8500000000),('Axie Infinity','axs','https://assets.coingecko.com/coins/images/13029/large/axie_infinity_logo.png?1604471082',5318027169.0000000000,270000000.0000000000,270000000.0000000000,69.0000000000),('Basic Attention Token','bat','https://assets.coingecko.com/coins/images/677/large/basic-attention-token.png?1547034427',1367898746.0000000000,1500000000.0000000000,1500000000.0000000000,0.9172410000),('Binance USD','busd','https://assets.coingecko.com/coins/images/9576/large/BUSD.png?1568947766',17537388168.0000000000,17566012245.9300000000,17566012245.9300000000,0.9981590000),('Bitcoin','btc','https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579',893095842948.0000000000,21000000.0000000000,21000000.0000000000,47012.0000000000),('Bitcoin Cash','bch','https://assets.coingecko.com/coins/images/780/large/bitcoin-cash-circle.png?1594689492',7208196392.0000000000,21000000.0000000000,21000000.0000000000,378.3900000000),('Bitcoin SV','bsv','https://assets.coingecko.com/coins/images/6799/large/BSV.png?1558947902',1858426127.0000000000,21000000.0000000000,21000000.0000000000,97.6700000000),('BitDAO','bit','https://assets.coingecko.com/coins/images/17627/large/bitdao.jpg?1628679607',1165734476.0000000000,10000000000.0000000000,10000000000.0000000000,1.3100000000),('BitTorrent','btt','https://assets.coingecko.com/coins/images/22457/large/btt_logo.png?1643857231',1964787203.0000000000,990000000000000.0000000000,990000000000000.0000000000,0.0000021400),('BNB','bnb','https://assets.coingecko.com/coins/images/825/large/bnb-icon2_2x.png?1644979850',72786905846.0000000000,168137035.9000000000,168137035.9000000000,433.0100000000),('Cardano','ada','https://assets.coingecko.com/coins/images/975/large/cardano.png?1547034860',38010855175.0000000000,45000000000.0000000000,45000000000.0000000000,1.1800000000),('cDAI','cdai','https://assets.coingecko.com/coins/images/9281/large/cDAI.png?1576467585',2053251175.0000000000,93810705478.2081000000,93810705478.2081000000,0.0218871700),('Celo','celo','https://assets.coingecko.com/coins/images/11090/large/icon-celo-CELO-color-500.png?1592293590',1428009043.0000000000,1000000000.0000000000,1000000000.0000000000,3.3400000000),('Celsius Network','cel','https://assets.coingecko.com/coins/images/3263/large/CEL_logo.png?1609598753',1435568074.0000000000,693942432.6871000000,693942432.6871000000,3.3900000000),('cETH','ceth','https://assets.coingecko.com/coins/images/10643/large/ceth2.JPG?1581389598',3570217364.0000000000,53590012.2255536000,53590012.2255536000,66.6200000000),('Chainlink','link','https://assets.coingecko.com/coins/images/877/large/chainlink-new-logo.png?1547034700',7966944522.0000000000,1000000000.0000000000,1000000000.0000000000,17.0500000000),('Chiliz','chz','https://assets.coingecko.com/coins/images/8834/large/Chiliz.png?1561970540',1447257940.0000000000,8888888888.0000000000,8888888888.0000000000,0.2706720000),('Convex Finance','cvx','https://assets.coingecko.com/coins/images/15585/large/convex.png?1621256328',1651959793.0000000000,87236177.7459302000,100000000.0000000000,29.9400000000),('Cosmos Hub','atom','https://assets.coingecko.com/coins/images/1481/large/cosmos_hub.png?1555657960',8852045487.0000000000,290994263.2149901400,290994263.2149901400,30.4200000000),('Cronos','cro','https://assets.coingecko.com/coins/images/7310/large/oCw2s3GI_400x400.jpeg?1645172042',12377789499.0000000000,30263013692.0000000000,30263013692.0000000000,0.4897820000),('cUSDC','cusdc','https://assets.coingecko.com/coins/images/9442/large/Compound_USDC.png?1567581577',2274098911.0000000000,100836918386.4390000000,100836918386.4390000000,0.0225522500),('Dai','dai','https://assets.coingecko.com/coins/images/9956/large/4943.png?1636636734',9229751710.0000000000,9243572220.3631300000,9243572220.3631300000,0.9979680000),('Dash','dash','https://assets.coingecko.com/coins/images/19/large/dash-logo.png?1548385930',1450940768.0000000000,18920000.0000000000,18920000.0000000000,136.1600000000),('Decentraland','mana','https://assets.coingecko.com/coins/images/878/large/decentraland-mana.png?1550108745',4159133105.0000000000,2193719627.3201500000,2193719627.3201500000,2.7500000000),('Dogecoin','doge','https://assets.coingecko.com/coins/images/5/large/dogecoin.png?1547792256',19901886380.0000000000,132544047604.7764600000,132544047604.7764600000,0.1501530000),('eCash','xec','https://assets.coingecko.com/coins/images/16646/large/Logo_final-22.png?1628239446',1859080664.0000000000,21000000000000.0000000000,21000000000000.0000000000,0.0000977100),('Elrond','egld','https://assets.coingecko.com/coins/images/12335/large/elrond3_360.png?1626341589',4609520511.0000000000,23419997.0000000000,23419997.0000000000,209.6300000000),('Enjin Coin','enj','https://assets.coingecko.com/coins/images/1102/large/enjin-coin-logo.png?1547035078',1697276692.0000000000,1000000000.0000000000,1000000000.0000000000,1.8200000000),('EOS','eos','https://assets.coingecko.com/coins/images/738/large/eos-eos-logo.png?1547034481',2950844431.0000000000,1000286247.7966101000,1000286247.7966101000,2.9500000000),('Ethereum','eth','https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880',399794949099.0000000000,120109761.2492414300,120109761.2492414300,3328.5800000000),('Ethereum Classic','etc','https://assets.coingecko.com/coins/images/453/large/ethereum-classic-logo.png?1547034169',6346964475.0000000000,210700000.0000000000,210700000.0000000000,47.4300000000),('Fantom','ftm','https://assets.coingecko.com/coins/images/4001/large/Fantom.png?1558015016',3678489807.0000000000,3175000000.0000000000,3175000000.0000000000,1.4500000000),('Filecoin','fil','https://assets.coingecko.com/coins/images/12817/large/filecoin.png?1602753933',4509777484.0000000000,1970528405.0000000000,1970528405.0000000000,24.5200000000),('Flow','flow','https://assets.coingecko.com/coins/images/13446/large/5f6294c0c7a8cda55cb1c936_Flow_Wordmark.png?1631696776',2513080421.0000000000,1411907590.7115800000,1411907590.7115800000,7.0300000000),('Frax','frax','https://assets.coingecko.com/coins/images/13422/large/frax_logo.png?1608476506',2686574379.0000000000,2690095597.8401200000,2690095597.8401200000,0.9976720000),('Frax Share','fxs','https://assets.coingecko.com/coins/images/13423/large/frax_share.png?1608478989',1233381214.0000000000,99247470.8138237000,99247470.8138237000,21.3400000000),('FTX Token','ftt','https://assets.coingecko.com/coins/images/9026/large/F.png?1609051564',7146768483.0000000000,333254663.5859720000,333254663.5859720000,51.9800000000),('Gala','gala','https://assets.coingecko.com/coins/images/12493/large/GALA-COINGECKO.png?1600233435',2043620742.0000000000,37152234822.3715000000,50000000000.0000000000,0.2705390000),('Harmony','one','https://assets.coingecko.com/coins/images/4344/large/Y88JAze.png?1565065793',2000777467.0000000000,13156044839.7931390000,13156044839.7931390000,0.1683980000),('Hedera','hbar','https://assets.coingecko.com/coins/images/3688/large/hbar.png?1637045634',4903991084.0000000000,50000000000.0000000000,50000000000.0000000000,0.2458560000),('Helium','hnt','https://assets.coingecko.com/coins/images/4284/large/Helium_HNT.png?1612620071',2501964201.0000000000,223000000.0000000000,223000000.0000000000,24.8600000000),('Holo','hot','https://assets.coingecko.com/coins/images/3348/large/Holologo_Profile.png?1547037966',1189375747.0000000000,177619433541.1410000000,177619433541.1410000000,0.0066895000),('Humans.ai','heart','https://assets.coingecko.com/coins/images/21273/large/h_logo_1x.png?1638858402',1309127902.0000000000,7800000000.0000000000,7800000000.0000000000,0.0497426600),('Huobi BTC','hbtc','https://assets.coingecko.com/coins/images/12407/large/Unknown-5.png?1599624896',1874884611.0000000000,39884.0822047420,39884.0822047420,47009.0000000000),('Huobi Token','ht','https://assets.coingecko.com/coins/images/2822/large/huobi-token-logo.png?1547036992',1415311948.0000000000,500000000.0000000000,500000000.0000000000,9.0800000000),('Internet Computer','icp','https://assets.coingecko.com/coins/images/14495/large/Internet_Computer_logo.png?1620703073',4878914368.0000000000,469213710.0000000000,469213710.0000000000,22.5300000000),('IOTA','miota','https://assets.coingecko.com/coins/images/692/large/IOTA_Swirl.png?1604238557',2480975708.0000000000,2779530283.0000000000,2779530283.0000000000,0.8940870000),('JUNO','juno','https://assets.coingecko.com/coins/images/19249/large/juno.png?1642838082',1293359159.0000000000,75916350.9286980000,185562268.0000000000,27.8300000000),('Kadena','kda','https://assets.coingecko.com/coins/images/3693/large/djLWD6mR_400x400.jpg?1591080616',1214504921.0000000000,1000000000.0000000000,1000000000.0000000000,7.0700000000),('Klaytn','klay','https://assets.coingecko.com/coins/images/9672/large/klaytn.jpeg?1642775250',3363294642.0000000000,2802745535.0000000000,2802745535.0000000000,1.2000000000),('KuCoin Token','kcs','https://assets.coingecko.com/coins/images/1047/large/sa9z79.png?1610678720',1459628987.0000000000,165879921.0000000000,165879921.0000000000,19.2500000000),('Kusama','ksm','https://assets.coingecko.com/coins/images/9568/large/m4zRhP5e_400x400.jpg?1576190080',1581822185.0000000000,10000000.0000000000,10000000.0000000000,176.5200000000),('LEO Token','leo','https://assets.coingecko.com/coins/images/8418/large/leo-token.png?1558326215',5738265601.0000000000,985239504.0000000000,985239504.0000000000,6.1400000000),('Lido Staked Ether','steth','https://assets.coingecko.com/coins/images/13442/large/steth_logo.png?1608607546',9375780016.0000000000,2819483.9108232700,2819483.9108232700,3328.2700000000),('Litecoin','ltc','https://assets.coingecko.com/coins/images/2/large/litecoin.png?1547033580',9183926835.0000000000,84000000.0000000000,84000000.0000000000,131.3000000000),('Loopring','lrc','https://assets.coingecko.com/coins/images/913/large/LRC.png?1572852344',1459582447.0000000000,1373873440.4424600000,1374513896.0000000000,1.1700000000),('Magic Internet Money','mim','https://assets.coingecko.com/coins/images/16786/large/mimlogopng.png?1624979612',2754737346.0000000000,2785296692.9794400000,2785296692.9794400000,0.9887600000),('Maker','mkr','https://assets.coingecko.com/coins/images/1364/large/Mark_Maker.png?1585191826',1922355926.0000000000,977631.0369508880,1005577.0000000000,2135.4800000000),('Mina Protocol','mina','https://assets.coingecko.com/coins/images/15628/large/JM4_vQ34_400x400.png?1621394004',1185802099.0000000000,904348252.8400390000,904348252.8400390000,2.7200000000),('Monero','xmr','https://assets.coingecko.com/coins/images/69/large/monero_logo.png?1547033729',3949669015.0000000000,18111932.0172421700,18111932.0172421700,218.0700000000),('Near','near','https://assets.coingecko.com/coins/images/10365/large/near_icon.png?1601359077',8715983221.0000000000,1000000000.0000000000,1000000000.0000000000,13.1800000000),('NEM','xem','https://assets.coingecko.com/coins/images/242/large/NEM_WC_Logo_200px.png?1642668663',1056302426.0000000000,8999999999.0000000000,8999999999.0000000000,0.1175790000),('NEO','neo','https://assets.coingecko.com/coins/images/480/large/NEO_512_512.png?1594357361',1882060794.0000000000,100000000.0000000000,100000000.0000000000,26.6800000000),('NEXO','nexo','https://assets.coingecko.com/coins/images/3695/large/nexo.png?1548086057',1349962288.0000000000,1000000000.0000000000,1000000000.0000000000,2.4100000000),('OKB','okb','https://assets.coingecko.com/coins/images/4463/large/WeChat_Image_20220118095654.png?1642471050',5814618405.0000000000,300000000.0000000000,300000000.0000000000,22.3300000000),('Osmosis','osmo','https://assets.coingecko.com/coins/images/16724/large/osmo.png?1632763885',2796604004.0000000000,325000000.0000000000,1000000000.0000000000,8.4600000000),('PancakeSwap','cake','https://assets.coingecko.com/coins/images/12632/large/pancakeswap-cake-logo_%281%29.png?1629359065',2366105151.0000000000,286107031.5598549000,286107031.5598549000,8.2700000000),('Polkadot','dot','https://assets.coingecko.com/coins/images/12171/large/polkadot.png?1639712644',25235540402.0000000000,1178295660.8258300000,1178295660.8258300000,22.9700000000),('Polygon','matic','https://assets.coingecko.com/coins/images/4713/large/matic-token-icon.png?1624446912',11791082783.0000000000,10000000000.0000000000,10000000000.0000000000,1.7200000000),('Quant','qnt','https://assets.coingecko.com/coins/images/3370/large/5ZOu7brX_400x400.jpg?1612437252',2045987165.0000000000,14612493.0000000000,14612493.0000000000,152.4100000000),('Radix','xrd','https://assets.coingecko.com/coins/images/4374/large/Radix.png?1629701658',1585662596.0000000000,12216630665.7333000000,24000000000.0000000000,0.1610090000),('Shiba Inu','shib','https://assets.coingecko.com/coins/images/11939/large/shiba.png?1622619446',14503151776.0000000000,1000000000000000.0000000000,1000000000000000.0000000000,0.0000264900),('Solana','sol','https://assets.coingecko.com/coins/images/4128/large/solana.png?1640133422',35557692179.0000000000,508180963.5700000000,508180963.5700000000,109.6400000000),('Stacks','stx','https://assets.coingecko.com/coins/images/2069/large/Stacks_logo_full.png?1604112510',1527887808.0000000000,1352464600.0000000000,1352464600.0000000000,1.4500000000),('Stellar','xlm','https://assets.coingecko.com/coins/images/100/large/Stellar_symbol_black_RGB.png?1552356157',5739213159.0000000000,50001788037.1491000000,50001788037.1491000000,0.2321020000),('Synthetix Network Token','snx','https://assets.coingecko.com/coins/images/3406/large/SNX.png?1598631139',1221709002.0000000000,248691562.6904490000,248691562.6904490000,5.6700000000),('Terra','luna','https://assets.coingecko.com/coins/images/8284/large/luna1557227471663.png?1567147072',33799545897.0000000000,753109642.5073490000,1000000000.0000000000,94.8500000000),('TerraUSD','ust','https://assets.coingecko.com/coins/images/12681/large/UST.png?1601612407',16201698169.0000000000,16222558573.8780000000,16222558573.8780000000,0.9982230000),('Tether','usdt','https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1598003707',81260616177.0000000000,81374736008.1639000000,81374736008.1639000000,0.9984400000),('Tezos','xtz','https://assets.coingecko.com/coins/images/976/large/Tezos-logo.png?1547034862',3450585504.0000000000,882502686.4450128000,882502686.4450128000,3.9100000000),('The Graph','grt','https://assets.coingecko.com/coins/images/13397/large/Graph_Token.png?1608145566',3069181838.0000000000,10000000000.0000000000,10000000000.0000000000,0.4577310000),('The Sandbox','sand','https://assets.coingecko.com/coins/images/12129/large/sandbox_logo.jpg?1597397942',4115680478.0000000000,3000000000.0000000000,3000000000.0000000000,3.5800000000),('Theta Fuel','tfuel','https://assets.coingecko.com/coins/images/8029/large/1_0YusgngOrriVg4ZYx4wOFQ.png?1553483622',1886178774.0000000000,5301200000.0000000000,5301200000.0000000000,0.1980980000),('Theta Network','theta','https://assets.coingecko.com/coins/images/2538/large/theta-token-logo.png?1548387191',3708483438.0000000000,1000000000.0000000000,1000000000.0000000000,3.7200000000),('THORChain','rune','https://assets.coingecko.com/coins/images/6595/large/RUNE.png?1614160507',3144893145.0000000000,500000000.0000000000,500000000.0000000000,10.4900000000),('TRON','trx','https://assets.coingecko.com/coins/images/1094/large/tron-logo.png?1547035066',7138213769.0000000000,101900409184.2730000000,101900409184.2730000000,0.0701980000),('TrueUSD','tusd','https://assets.coingecko.com/coins/images/3449/large/tusd.png?1618395665',1360038270.0000000000,1362177116.0602600000,1362177116.0602600000,0.9981510000),('Uniswap','uni','https://assets.coingecko.com/coins/images/12504/large/uniswap-uni.png?1600306604',5162325318.0000000000,1000000000.0000000000,1000000000.0000000000,11.3100000000),('USD Coin','usdc','https://assets.coingecko.com/coins/images/6319/large/USD_Coin_icon.png?1547042389',52086347240.0000000000,52076008581.9405000000,52076008581.9405000000,1.0000000000),('VeChain','vet','https://assets.coingecko.com/coins/images/1167/large/VeChain-Logo-768x725.png?1547035194',5176454703.0000000000,86712634466.0000000000,86712634466.0000000000,0.0783730000),('Waves','waves','https://assets.coingecko.com/coins/images/425/large/waves.png?1548386117',3185870417.0000000000,100000000.0000000000,100000000.0000000000,31.8700000000),('Wrapped Bitcoin','wbtc','https://assets.coingecko.com/coins/images/7598/large/wrapped_bitcoin_wbtc.png?1548822744',12895859877.0000000000,274230.4660879400,274230.4660879400,47098.0000000000),('XRP','xrp','https://assets.coingecko.com/coins/images/44/large/xrp-symbol-white-128.png?1605778731',41590190970.0000000000,100000000000.0000000000,100000000000.0000000000,0.8638370000),('Zcash','zec','https://assets.coingecko.com/coins/images/486/large/circle-zcash-color.png?1547034197',2515204513.0000000000,21000000.0000000000,21000000.0000000000,204.8900000000),('Zilliqa','zil','https://assets.coingecko.com/coins/images/2687/large/Zilliqa-logo.png?1547036894',1636062834.0000000000,21000000000.0000000000,21000000000.0000000000,0.1166660000);
/*!40000 ALTER TABLE `token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tokenhistory`
--

DROP TABLE IF EXISTS `tokenhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tokenhistory` (
  `TokenHistoryID` int NOT NULL AUTO_INCREMENT,
  `TokenName` varchar(50) NOT NULL,
  `Volume` double(30,10) NOT NULL,
  PRIMARY KEY (`TokenHistoryID`),
  KEY `fk_TokenHistory_Token` (`TokenName`),
  CONSTRAINT `fk_TokenHistory_Token` FOREIGN KEY (`TokenName`) REFERENCES `token` (`TokenName`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `TokenVolumePositive` CHECK ((`Volume` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tokenhistory`
--

LOCK TABLES `tokenhistory` WRITE;
/*!40000 ALTER TABLE `tokenhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `tokenhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `UserName` varchar(50) NOT NULL,
  `PassWord` varchar(100) NOT NULL,
  `UserBio` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`UserName`),
  UNIQUE KEY `UserName` (`UserName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('dung','string',''),('duyen','string',''),('hien','string',''),('huy','string',''),('ming','string','abcd');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userbalance`
--

DROP TABLE IF EXISTS `userbalance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userbalance` (
  `UserName` varchar(50) NOT NULL,
  `TokenName` varchar(50) NOT NULL,
  `Amount` double(30,10) NOT NULL,
  PRIMARY KEY (`UserName`,`TokenName`),
  KEY `fk_UserBalance_Token` (`TokenName`),
  CONSTRAINT `fk_UserBalance_Token` FOREIGN KEY (`TokenName`) REFERENCES `token` (`TokenName`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_UserBalance_User` FOREIGN KEY (`UserName`) REFERENCES `user` (`UserName`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `UserBalanceAmountPositive` CHECK ((`Amount` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userbalance`
--

LOCK TABLES `userbalance` WRITE;
/*!40000 ALTER TABLE `userbalance` DISABLE KEYS */;
INSERT INTO `userbalance` VALUES ('dung','Bitcoin',500.0000000000),('duyen','Bitcoin',20.0000000000),('duyen','Terra',495.0000000000),('hien','Bitcoin',480.0000000000),('hien','Terra',300.0000000000),('huy','Terra',500.0000000000),('ming','Bitcoin',495.0000000000),('ming','Terra',250.0000000000);
/*!40000 ALTER TABLE `userbalance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-24  0:44:13

SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=1;