--SQL file generated using MySQL Workbench for Linux
SET NAMES utf8;

DROP TABLE IF EXISTS `contacts`;
CREATE TABLE `contacts` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `lastname` varchar(32) NOT NULL,
  `picture` varchar(128) NOT NULL,
  `address` varchar(256) NOT NULL,
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `fk_book_users1_idx` (`uid`),
  CONSTRAINT `fk_book_users1` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `contact_sn`;
CREATE TABLE `contact_sn` (
  `snid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`snid`,`cid`),
  KEY `fk_social_networks_has_book_book1_idx` (`cid`),
  KEY `fk_social_networks_has_book_social_networks1_idx` (`snid`),
  CONSTRAINT `fk_social_networks_has_book_social_networks1` FOREIGN KEY (`snid`) REFERENCES `social_networks` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_social_networks_has_book_book1` FOREIGN KEY (`cid`) REFERENCES `book` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `custom_fields`;
CREATE TABLE `custom_fields` (
  `id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `field` varchar(32) NOT NULL,
  `value` varchar(128) NOT NULL,
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_custom_fields_book1_idx` (`cid`),
  CONSTRAINT `fk_custom_fields_book1` FOREIGN KEY (`cid`) REFERENCES `book` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `email_type`;
CREATE TABLE `email_type` (
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `email_type` (`name`) VALUES
('CUSTOM'),
('HOME'),
('OTHER'),
('PERSONAL'),
('WORK');

DROP TABLE IF EXISTS `emails`;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `email` varchar(45) NOT NULL,
  `type` varchar(32) NOT NULL DEFAULT 'PERSONAL' COMMENT 'PERSONAL, WORK, OTHER',
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index4` (`cid`,`email`),
  KEY `fk_table1_book_idx` (`cid`),
  KEY `index3` (`email`),
  CONSTRAINT `fk_table1_book` FOREIGN KEY (`cid`) REFERENCES `book` (`cid`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `phone_types`;
CREATE TABLE `phone_types` (
  `name` varchar(16) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `phone_types` (`name`) VALUES
('CUSTOM'),
('FAX'),
('HOME'),
('MAIN'),
('MOBILE'),
('OTHER'),
('WORK');

DROP TABLE IF EXISTS `phones`;
CREATE TABLE `phones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) NOT NULL,
  `phone` varchar(16) NOT NULL,
  `type` varchar(32) NOT NULL DEFAULT 'MOBILE' COMMENT 'MOBILE, WORK, HOME, OTHER, CUSTOM',
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_table1_book1_idx` (`cid`),
  CONSTRAINT `fk_table1_book1` FOREIGN KEY (`cid`) REFERENCES `book` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `social_networks`;
CREATE TABLE `social_networks` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `url` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `social_networks` (`id`, `name`, `url`) VALUES
(1,	'Facebook',	'http://www.facebook.com'),
(2,	'Twitter',	'http://www.twitter.com'),
(3,	'Instagram',	'http://www.instagram.com');

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `uid` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `mobile` varchar(16) NOT NULL,
  `email` varchar(64) NOT NULL,
  `password` varchar(45) NOT NULL,
  `modification` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `creation` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
