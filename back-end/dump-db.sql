-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: 141.94.203.217    Database: db
-- ------------------------------------------------------
-- Server version	5.5.5-10.6.5-MariaDB-1:10.6.5+maria~focal

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
-- Table structure for table `cita`
--

DROP TABLE IF EXISTS `cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cita` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_trabajo` int(11) DEFAULT NULL,
  `fecha` datetime NOT NULL,
  `id_certificado` int(11) DEFAULT NULL,
  `id_tecnico` int(11) DEFAULT NULL,
  `id_perito` int(11) DEFAULT NULL,
  `id_administrador` int(11) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cita`
--

LOCK TABLES `cita` WRITE;
/*!40000 ALTER TABLE `cita` DISABLE KEYS */;
INSERT INTO `cita` VALUES (1,1,'2022-02-11 09:10:00',NULL,NULL,4,NULL,'Revisión final','Calle Japon 2 6A'),(2,1,'2022-02-07 10:00:00',NULL,1,NULL,NULL,'Peritaje del trabajo','Calle Japon 2 6A'),(3,1,'2022-02-09 09:00:00',NULL,1,NULL,NULL,'Reparación completa','Calle Japon 5 4A'),(4,NULL,'2022-02-15 09:00:00',NULL,1,NULL,NULL,'Peritaje nuevo','Calle de prueba'),(5,NULL,'2022-03-10 08:46:00',NULL,NULL,NULL,2,'Curva lactosa niña - planta 1','Hptal. Virgen Macarena');
/*!40000 ALTER TABLE `cita` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `id_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `clientePotencial` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,11,0);
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `externalworkers`
--

DROP TABLE IF EXISTS `externalworkers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `externalworkers` (
  `id_ext` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `ocupacion` text COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id_ext`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `externalworkers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `externalworkers`
--

LOCK TABLES `externalworkers` WRITE;
/*!40000 ALTER TABLE `externalworkers` DISABLE KEYS */;
INSERT INTO `externalworkers` VALUES (1,7,'Ferretero');
/*!40000 ALTER TABLE `externalworkers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestor`
--

DROP TABLE IF EXISTS `gestor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gestor` (
  `id_gestor` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id_gestor`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `gestor_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestor`
--

LOCK TABLES `gestor` WRITE;
/*!40000 ALTER TABLE `gestor` DISABLE KEYS */;
INSERT INTO `gestor` VALUES (2,9),(3,12);
/*!40000 ALTER TABLE `gestor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materials` (
  `nombre` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `stockSeguridad` int(11) NOT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materials`
--

LOCK TABLES `materials` WRITE;
/*!40000 ALTER TABLE `materials` DISABLE KEYS */;
INSERT INTO `materials` VALUES ('Arandelas',210,50),('Tubo',10,2),('Tuerca 10mm',28,5);
/*!40000 ALTER TABLE `materials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajo`
--

DROP TABLE IF EXISTS `trabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trabajo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` enum('Instalacion de agua','Instalacion de gas','Revision de agua','Revision de gas','Reparacion','otro') CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `descripcion` text NOT NULL,
  `direccion` text NOT NULL,
  `id_cliente` int(11) NOT NULL,
  `id_certificado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajo`
--

LOCK TABLES `trabajo` WRITE;
/*!40000 ALTER TABLE `trabajo` DISABLE KEYS */;
INSERT INTO `trabajo` VALUES (1,'Instalacion de agua','Instalación de agua de cocina completa con grifo y salida para patio de exterior','Calle Japon 5 4A',11,NULL),(2,'Revision de agua','Revisión de la instalación','Calle Japon 5 4A',11,NULL),(3,'Revision de agua','Esto es una prueba','jander clander',11,NULL);
/*!40000 ALTER TABLE `trabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id_persona` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `apellidos` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `dni` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `email` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `direccion` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `telefono` bigint(20) NOT NULL,
  PRIMARY KEY (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3,'David','Brincau Cano','29506399K','david.brincau@hotmail.com','Calle vedra Nº1',678623620),(4,'Admin','Admin User','00000000X','admin@david&cia.com','SE',999999999),(7,'Jesus','Aparicio','25978463P','troapasej@us.es','Calle de test',601072573),(9,'Gestor nombre','apellidos gestor','28497845Ñ','gestor@david&cia.com','Avda Reina Mercedes 2 2ºB',678542985),(11,'Carmen','Muñoz Perez','28675432P','carmunper1@alum.us.es','Calle Japon 2 6A',673600485),(12,'Luis','Marin','24589678Ñ','sin mail','sin especificar',670123456);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workers`
--

DROP TABLE IF EXISTS `workers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pass` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `tipo` enum('Administrador','Perito','Técnico') COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `workers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_persona`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workers`
--

LOCK TABLES `workers` WRITE;
/*!40000 ALTER TABLE `workers` DISABLE KEYS */;
INSERT INTO `workers` VALUES (1,'0T234T6T897TcT11f5disKl21oñlPq17',3,'Técnico'),(2,'contraseña',4,'Administrador'),(4,'Peritisimo',3,'Perito');
/*!40000 ALTER TABLE `workers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-02 11:40:05
