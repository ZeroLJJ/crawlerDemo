/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.20 : Database - zhilian
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`zhilian` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `zhilian`;

/*Table structure for table `recruitment` */

DROP TABLE IF EXISTS `recruitment`;

CREATE TABLE `recruitment` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `company_name` varchar(100) DEFAULT NULL COMMENT '公司名',
  `company_type` varchar(20) DEFAULT NULL COMMENT '公司类型',
  `company_num` varchar(100) DEFAULT NULL COMMENT '公司人数',
  `job_name` varchar(100) DEFAULT NULL COMMENT '岗位名',
  `salary` varchar(50) DEFAULT NULL COMMENT '薪酬',
  `address` varchar(50) DEFAULT NULL COMMENT '工作地点',
  `experience` varchar(50) DEFAULT NULL COMMENT '工作经验',
  `education` varchar(20) DEFAULT NULL COMMENT '教育',
  `welfare` varchar(200) DEFAULT NULL COMMENT '福利',
  `url` varchar(500) DEFAULT NULL COMMENT '招聘链接',
  `if_eager` tinyint(1) DEFAULT NULL COMMENT '是否求贤若渴',
  `status` varchar(20) DEFAULT NULL COMMENT '招聘状态',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8;

/*Data for the table `recruitment` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
