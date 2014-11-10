-- Fix AUTOINCREMENT
ALTER TABLE `users` CHANGE `uid` `uid` int(11) NOT NULL AUTO_INCREMENT FIRST;
ALTER TABLE `custom_fields` CHANGE `id` `id` int(11) NOT NULL AUTO_INCREMENT FIRST;

-- Add missing field
ALTER TABLE `contact_sn` ADD `username` varchar(64) NOT NULL AFTER `cid`



ALTER TABLE  `contact_sn` DROP FOREIGN KEY  `fk_social_networks_has_book_book1` ;
ALTER TABLE  `contact_sn` ADD CONSTRAINT  `fk_social_networks_has_book_book1` FOREIGN KEY (  `cid` ) REFERENCES  `address_book`.`contacts` (
`cid`) ON DELETE CASCADE ON UPDATE NO ACTION ;

ALTER TABLE  `custom_fields` DROP FOREIGN KEY  `fk_custom_fields_book1` ;
ALTER TABLE  `custom_fields` ADD CONSTRAINT  `fk_custom_fields_book1` FOREIGN KEY (  `cid` ) REFERENCES  `address_book`.`contacts` (
`cid`) ON DELETE CASCADE ON UPDATE NO ACTION ;

ALTER TABLE  `phones` DROP FOREIGN KEY  `fk_table1_book1` ;
ALTER TABLE  `phones` ADD CONSTRAINT  `fk_table1_book1` FOREIGN KEY (  `cid` ) REFERENCES  `address_book`.`contacts` (
`cid`) ON DELETE CASCADE ON UPDATE NO ACTION ;

ALTER TABLE  `contacts` DROP FOREIGN KEY  `fk_book_users1` ;
ALTER TABLE  `contacts` ADD CONSTRAINT  `fk_book_users1` FOREIGN KEY (  `uid` ) REFERENCES  `address_book`.`users` (
`uid`) ON DELETE RESTRICT ON UPDATE NO ACTION ;
