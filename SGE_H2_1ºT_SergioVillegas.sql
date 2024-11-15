DROP DATABASE IF EXISTS ENCUESTAS;
CREATE DATABASE ENCUESTAS;
USE ENCUESTAS;

CREATE TABLE ENCUESTA (
	idEncuesta int primary key,
    edad int,
    Sexo varchar(7),
	BebidasSemana int,
    CervezasSemana int,
	BebidasFinSemana int, 
    BebidasDestiladasSemana	int,
    VinosSemana	int, 
    PerdidasControl int, 
    DiversionDependenciaAlcohol	char(2),
    ProblemasDigestivos	char(2),
    TensionAlta	char(12),
    DolorCabeza char(12)
);


INSERT INTO `encuesta` VALUES (1,57,'Mujer',5,5,5,0,3,1,'No','Sí','No lo se','Alguna vez'),(2,55,'Mujer',6,4,5,1,2,3,'Sí','Sí','No','Alguna vez'),(3,19,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(4,20,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(5,21,'Hombre',20,15,10,5,0,12,'Sí','No','No','Alguna vez'),(6,20,'Hombre',1,12,45,12,23,45,'No','No','No','Alguna vez'),(7,19,'Hombre',2,0,2,2,0,3,'No','No','No','Nunca'),(8,19,'Hombre',3,5,5,5,0,1,'Sí','No','No lo se','Muy a menudo'),(9,22,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(10,19,'Hombre',2,10,5,1,5,2,'No','No','No','Alguna vez'),(11,19,'Hombre',83,0,75,27,56,33,'Sí','Sí','Sí','Muy a menudo'),(12,21,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(13,19,'Hombre',5,5,5,5,0,1,'Sí','No','No lo se','Alguna vez'),(14,24,'Hombre',25,18,10,7,0,365,'No','No','No','Alguna vez'),(15,38,'Mujer',41,5,25,10,10,365,'Sí','Sí','Sí','Muy a menudo'),(16,53,'Mujer',0,0,0,0,0,0,'No','No','Sí','Alguna vez'),(17,19,'Hombre',4,0,1,1,1,1,'No','No','No','Nunca'),(18,20,'Hombre',3,7,7,2,0,0,'Sí','Sí','No lo se','Nunca'),(19,20,'Hombre',3,2,5,3,0,1,'No','No','No','Alguna vez'),(20,21,'Mujer',2,0,2,0,2,0,'No','No','No','A menudo'),(21,19,'Hombre',20,20,10,7,0,3,'No','No','No lo se','Alguna vez'),(22,20,'Hombre',1,0,0,1,1,0,'No','No','No','Nunca'),(23,19,'Hombre',0,0,0,0,0,0,'No','No','Sí','Alguna vez'),(24,58,'Hombre',12,6,7,4,3,2,'No','Sí','Sí','A menudo'),(25,47,'Hombre',0,0,3,3,0,2,'No','No','No','Nunca'),(26,19,'Hombre',1,0,5,1,0,5,'Sí','No','No','Nunca'),(27,37,'Mujer',10,5,6,3,3,3,'Sí','Sí','Sí','Muy a menudo'),(28,50,'Hombre',50,35,65,26,1,100,'Sí','Sí','Sí','Muy a menudo'),(29,19,'Hombre',0,0,0,0,0,0,'No','Sí','No','Alguna vez'),(30,19,'Hombre',23,0,10,11,12,69,'Sí','No','No','A menudo'),(31,19,'Hombre',0,0,0,0,0,3,'No','No','No lo se','Nunca'),(32,60,'Mujer',3,2,3,0,1,0,'No','Sí','Sí','A menudo'),(33,25,'Hombre',7,2,7,5,0,0,'No','No','No','A menudo'),(34,45,'Mujer',10,3,5,3,0,1,'Sí','Sí','No lo se','Muy a menudo'),(35,53,'Mujer',3,3,3,0,1,0,'No','Sí','No','Muy a menudo'),(36,55,'Hombre',11,5,4,0,2,0,'No','No','No','Nunca'),(37,18,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(38,55,'Mujer',0,0,4,0,4,0,'No','Sí','No','Muy a menudo'),(39,56,'Hombre',3,2,2,0,3,2,'Sí','No','Sí','Nunca'),(40,61,'Hombre',6,2,4,1,3,0,'No','No','No','Nunca'),(41,37,'Hombre',4,1,2,0,3,0,'No','No','No','Nunca'),(42,56,'Mujer',2,5,4,0,2,1,'No','Sí','Sí','Alguna vez'),(43,71,'Hombre',2,1,1,0,1,0,'No','No','No','Alguna vez'),(44,36,'Hombre',8,8,8,0,0,0,'No','No','No','Alguna vez'),(45,67,'Hombre',67,7,2,0,0,0,'No','No','No lo se','Nunca'),(46,33,'Mujer',1,4,6,0,0,2,'No','Sí','No','A menudo'),(47,71,'Mujer',2,2,2,0,0,0,'No','No','No','Nunca'),(48,52,'Hombre',6,6,3,0,0,0,'No','Sí','No lo se','Alguna vez'),(49,41,'Hombre',6,6,6,0,0,0,'No','No','No lo se','Alguna vez'),(50,41,'Mujer',2,1,2,0,1,2,'No','No','No','Nunca'),(51,38,'Mujer',1,1,1,0,1,0,'No','Sí','No','Alguna vez'),(52,63,'Mujer',0,0,0,0,0,0,'No','No','No','Alguna vez'),(53,60,'Mujer',1,0,1,0,1,0,'No','No','No','Alguna vez'),(54,34,'Mujer',1,1,1,0,0,0,'No','Sí','No','Alguna vez'),(55,41,'Mujer',10,10,10,0,0,0,'No','No','No','Alguna vez'),(56,31,'Mujer',0,0,6,6,0,2,'No','Sí','No','Alguna vez'),(57,35,'Hombre',11,6,9,2,5,0,'No','No','No','Nunca'),(58,50,'Hombre',5,1,1,0,4,0,'No','No','No','Nunca'),(59,46,'Mujer',14,1,8,3,6,0,'Sí','Sí','No','Alguna vez'),(60,36,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(61,54,'Mujer',5,4,5,0,3,0,'Sí','No','No','Alguna vez'),(62,65,'Mujer',0,0,0,0,0,0,'No','No','No','Nunca'),(63,41,'Mujer',0,0,0,0,0,0,'No','Sí','No','Muy a menudo'),(64,44,'Mujer',2,2,2,0,0,0,'No','No','No','Alguna vez'),(65,61,'Mujer',1,0,1,0,0,0,'No','No','No','Alguna vez'),(66,63,'Hombre',2,0,4,0,6,0,'No','Sí','Sí','Alguna vez'),(67,47,'Hombre',2,2,2,0,1,0,'No','No','No','Alguna vez'),(68,30,'Mujer',2,0,2,0,2,1,'No','No','No lo se','Alguna vez'),(69,44,'Mujer',0,0,2,0,0,1,'No','Sí','No','Alguna vez'),(70,45,'Mujer',0,0,0,0,0,0,'No','No','No','Alguna vez'),(71,44,'Mujer',1,1,1,0,0,0,'No','No','No','Alguna vez'),(72,43,'Mujer',0,0,0,0,0,0,'No','No','No','Nunca'),(73,38,'Mujer',0,0,0,0,0,0,'No','No','No','Nunca'),(74,27,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(75,47,'Hombre',3,3,3,1,1,1,'No','No','Sí','Alguna vez'),(76,47,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(77,52,'Hombre',0,5,1,1,0,10,'No','No','No','Alguna vez'),(78,45,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Nunca'),(79,16,'Mujer',0,0,0,0,0,0,'No','No','No','A menudo'),(80,16,'Mujer',5,30,15,5,6,4,'No','No','No lo se','Muy a menudo'),(81,16,'Mujer',0,0,0,0,0,1,'No','No','No lo se','Muy a menudo'),(82,19,'Mujer',0,0,0,0,0,0,'No','No','No','Muy a menudo'),(83,17,'Mujer',0,0,0,0,0,0,'No','No','No lo se','A menudo'),(84,16,'Mujer',0,0,0,0,0,0,'No','No','No','Alguna vez'),(85,15,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(86,16,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(87,16,'Hombre',1,1,0,0,2,2,'Sí','No','No','Alguna vez'),(88,17,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(89,15,'Mujer',0,0,0,0,0,2,'No','No','No lo se','Muy a menudo'),(90,16,'Hombre',0,0,0,3,0,0,'No','No','No','Alguna vez'),(91,15,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(92,17,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(93,17,'Mujer',0,0,0,0,0,0,'No','No','No','Alguna vez'),(94,59,'Hombre',6,4,4,0,2,0,'No','Sí','No','Alguna vez'),(95,18,'Hombre',0,0,0,0,2,0,'No','No','No lo se','Alguna vez'),(96,17,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(97,16,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(98,18,'Hombre',0,0,0,0,0,1,'No','No','No lo se','Nunca'),(99,17,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Nunca'),(100,17,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(101,17,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Nunca'),(102,15,'Hombre',0,0,0,0,0,0,'No','No','No lo se','A menudo'),(103,59,'Hombre',0,0,0,0,0,1,'No','No','No','Nunca'),(104,17,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(105,15,'Mujer',0,0,0,0,0,1,'No','No','No lo se','Muy a menudo'),(106,17,'Mujer',0,0,0,0,0,0,'No','Sí','No lo se','Alguna vez'),(107,15,'Mujer',0,0,0,0,0,0,'No','Sí','No lo se','Muy a menudo'),(108,15,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(109,19,'Hombre',0,0,0,0,0,0,'No','Sí','No lo se','A menudo'),(110,26,'Hombre',0,0,0,0,0,1,'No','No','No','Alguna vez'),(111,18,'Hombre',0,0,0,0,0,0,'No','No','No lo se','A menudo'),(112,18,'Hombre',2,2,0,0,0,1,'No','No','No lo se','Alguna vez'),(113,18,'Hombre',0,0,4,0,0,1,'No','No','No lo se','Alguna vez'),(114,18,'Hombre',0,0,0,0,0,0,'No','No','No','A menudo'),(115,18,'Hombre',0,0,0,0,0,1,'No','No','No','Alguna vez'),(116,25,'Mujer',5,2,5,2,0,1,'No','No','No','A menudo'),(117,18,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(118,18,'Hombre',3,4,6,3,0,2,'No','Sí','No lo se','Alguna vez'),(119,19,'Hombre',2,3,3,3,0,1,'Sí','No','No lo se','Alguna vez'),(120,18,'Hombre',2,4,5,1,0,3,'No','Sí','No lo se','Alguna vez'),(121,38,'Mujer',0,0,0,0,2,2,'No','No','No lo se','Alguna vez'),(122,18,'Hombre',5,2,2,2,0,2,'No','No','No','Muy a menudo'),(123,18,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(124,20,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Nunca'),(125,18,'Hombre',3,6,6,2,1,0,'No','No','No','Alguna vez'),(126,18,'Hombre',4,3,6,6,0,4,'No','No','No lo se','Alguna vez'),(127,20,'Hombre',6,5,3,0,0,0,'No','Sí','No','Alguna vez'),(128,19,'Mujer',0,5,5,0,0,0,'No','No','No lo se','Nunca'),(129,26,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(130,33,'Mujer',10,6,15,10,1,2,'Sí','Sí','No lo se','Alguna vez'),(131,15,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(132,18,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(133,18,'Mujer',0,0,0,0,0,0,'No','No','No','Alguna vez'),(134,28,'Hombre',1,0,1,1,0,0,'No','No','No','Nunca'),(135,18,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Muy a menudo'),(136,28,'Mujer',1,0,3,0,3,0,'No','Sí','No','Muy a menudo'),(137,18,'Hombre',1,1,1,1,1,0,'No','No','No','Nunca'),(138,18,'Hombre',3,4,5,1,1,1,'No','No','No lo se','Alguna vez'),(139,19,'Hombre',8,2,8,2,0,20,'No','No','No lo se','Muy a menudo'),(140,21,'Hombre',6,4,6,4,0,0,'No','No','No lo se','Nunca'),(141,33,'Hombre',33,12,18,5,4,3,'Sí','Sí','Sí','Muy a menudo'),(142,19,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(143,58,'Mujer',12,7,6,2,3,5,'Sí','Sí','Sí','Muy a menudo'),(144,62,'Mujer',18,5,8,4,3,4,'No','Sí','Sí','Muy a menudo'),(145,60,'Hombre',26,12,10,4,7,6,'Sí','No','Sí','A menudo'),(146,21,'Hombre',3,2,3,1,0,1,'No','Sí','No','Muy a menudo'),(147,21,'Mujer',0,0,0,0,0,6,'Sí','No','No','Nunca'),(148,40,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(149,25,'Hombre',0,0,0,0,0,0,'No','Sí','No lo se','Alguna vez'),(150,22,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(151,20,'Hombre',0,0,0,0,0,0,'No','No','Sí','A menudo'),(152,19,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(153,22,'Hombre',4,0,5,4,2,0,'No','Sí','No','Alguna vez'),(154,19,'Hombre',50,15,30,10,0,2,'No','No','No lo se','Nunca'),(155,20,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(156,22,'Hombre',5,4,3,1,0,10,'No','No','No','Alguna vez'),(157,21,'Hombre',0,1,0,0,0,0,'No','No','No','Nunca'),(158,20,'Hombre',0,0,0,0,0,3,'No','No','No','Alguna vez'),(159,21,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(160,23,'Hombre',2,2,2,0,0,0,'No','No','No','Alguna vez'),(161,21,'Mujer',1,1,0,0,0,0,'No','Sí','No','Alguna vez'),(162,18,'Hombre',0,1,2,0,2,1,'Sí','No','No','Alguna vez'),(163,20,'Hombre',0,0,3,3,0,0,'No','No','No lo se','Nunca'),(164,19,'Hombre',3,32,3,0,0,0,'No','No','No','Alguna vez'),(165,23,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(166,19,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(167,16,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(168,22,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(169,23,'Hombre',0,0,0,0,0,1,'No','Sí','No','Alguna vez'),(170,19,'Hombre',2,1,2,2,0,3,'Sí','No','No lo se','Alguna vez'),(171,23,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(172,20,'Hombre',5,5,2,2,0,5,'No','No','No lo se','Alguna vez'),(173,23,'Hombre',11,6,9,6,0,3,'Sí','No','No lo se','Alguna vez'),(174,22,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(175,34,'Mujer',0,0,0,0,0,0,'No','Sí','No','Muy a menudo'),(176,18,'Hombre',1,0,0,1,0,0,'No','No','No','Alguna vez'),(177,20,'Hombre',6,7,12,6,0,2,'No','No','No','Alguna vez'),(178,21,'Hombre',0,0,0,0,0,0,'No','No','No lo se','A menudo'),(179,19,'Hombre',2,0,2,0,0,0,'No','No','No','A menudo'),(180,18,'Mujer',1,1,1,0,0,0,'No','No','No','Nunca'),(181,18,'Hombre',0,0,0,0,0,0,'No','Sí','No','Alguna vez'),(182,18,'Hombre',4,2,1,1,0,5,'No','No','No','Nunca'),(183,19,'Mujer',1,4,0,0,0,2,'No','Sí','No','Muy a menudo'),(184,25,'Hombre',2,2,2,0,0,0,'No','No','No','Alguna vez'),(185,19,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(186,35,'Hombre',2,2,0,0,0,0,'No','No','No','Alguna vez'),(187,18,'Hombre',5,3,4,1,4,0,'No','Sí','No','A menudo'),(188,16,'Hombre',0,0,0,0,0,0,'No','No','No lo se','A menudo'),(189,18,'Mujer',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(190,17,'Hombre',0,0,0,0,0,2,'No','No','No','A menudo'),(191,17,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(192,18,'Hombre',1,1,2,1,0,0,'No','No','No','Alguna vez'),(193,20,'Hombre',0,0,0,0,0,0,'No','Sí','Sí','A menudo'),(194,19,'Hombre',3,3,3,0,0,0,'No','No','No','Alguna vez'),(195,20,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(196,20,'Hombre',19,12,9,2,2,4,'Sí','No','No lo se','Nunca'),(197,19,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez'),(198,32,'Hombre',54,17,12,7,4,38,'Sí','No','No lo se','Alguna vez'),(199,21,'Hombre',0,0,0,0,0,1,'No','No','No lo se','Alguna vez'),(200,22,'Hombre',8,7,10,13,4,5,'Sí','No','No','Nunca'),(201,22,'Hombre',0,1,1,0,0,0,'No','No','No','Alguna vez'),(202,20,'Hombre',1,0,1,1,0,5,'No','No','No','Alguna vez'),(203,20,'Hombre',10,2,8,8,5,25,'No','Sí','No lo se','Alguna vez'),(204,22,'Hombre',10,8,2,1,0,15,'No','No','No lo se','Nunca'),(205,24,'Hombre',0,0,0,0,0,0,'Sí','No','No','Nunca'),(206,21,'Hombre',0,0,0,0,0,0,'No','No','No','Nunca'),(207,19,'Hombre',0,0,0,0,0,0,'No','No','No','Alguna vez'),(208,20,'Hombre',0,3,0,0,0,3,'No','No','No lo se','Alguna vez'),(209,21,'Hombre',0,0,0,0,2,0,'No','No','No','Alguna vez'),(210,19,'Hombre',5,2,3,2,0,2,'No','No','No','Alguna vez'),(211,20,'Hombre',3,4,3,2,0,0,'No','No','No','Nunca'),(212,20,'Hombre',20,15,10,8,0,100,'Sí','Sí','No lo se','Muy a menudo'),(213,20,'Hombre',2,10,15,20,5,4,'No','No','No','Alguna vez'),(214,19,'Hombre',69,40,30,8,12,69,'Sí','Sí','Sí','Muy a menudo'),(215,21,'Hombre',5,1,1,1,0,2,'No','No','No','A menudo'),(216,20,'Hombre',0,0,0,0,0,0,'No','No','No lo se','Alguna vez');
select*from encuesta;