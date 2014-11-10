-- Test data
INSERT INTO `users` (`uid`, `name`, `mobile`, `email`, `password`, `modification`, `creation`) VALUES
(1, 'Test user', '1234567890', 'test@gmail.com', sha1('qwerty'), now(), now());

INSERT INTO `contacts` (`cid`, `uid`, `name`, `lastname`, `picture`, `address`, `modification`, `creation`)
VALUES ('1', '1', 'John', 'Doe', 'http://tinyurl.com/a39ukxn', 'Address Known', now(), now());

INSERT INTO `phones` (`cid`, `phone`, `type`, `modification`, `creation`)
VALUES ('1', '1234567890', 'MOBILE', now(), now());

INSERT INTO `contact_sn` (`snid`, `cid`, `username`, `modification`, `creation`)
VALUES ('2', '1', 'py3k', now(), now());

INSERT INTO `emails` (`cid`, `email`, `type`, `modification`, `creation`)
VALUES ('1', 'contact@mail.net', 'PERSONAL', now(), now());

INSERT INTO `custom_fields` (`cid`, `field`, `value`, `modification`, `creation`)
VALUES ('1', 'nickname', 'Pulparindo', now(), now());

INSERT INTO `custom_fields` (`cid`, `field`, `value`, `modification`, `creation`)
VALUES ('1', 'group', 'school, work', now(), now());



INSERT INTO `contacts` (`cid`, `uid`, `name`, `lastname`, `picture`, `address`, `modification`, `creation`)
VALUES ('2', '1', 'Homer', 'Simpson', 'http://tinyurl.com/a39ukxn', 'Address Known', now(), now());

INSERT INTO `phones` (`cid`, `phone`, `type`, `modification`, `creation`)
VALUES ('2', '1234567890', 'MOBILE', now(), now());

INSERT INTO `phones` (`cid`, `phone`, `type`, `modification`, `creation`)
VALUES ('2', '1236587458', 'WORK', now(), now());

INSERT INTO `contact_sn` (`snid`, `cid`, `username`, `modification`, `creation`)
VALUES ('1', '2', 'homersimpson', now(), now());

INSERT INTO `contact_sn` (`snid`, `cid`, `username`, `modification`, `creation`)
VALUES ('2', '2', 'homersimpson', now(), now());

INSERT INTO `emails` (`cid`, `email`, `type`, `modification`, `creation`)
VALUES ('2', 'homer@simpson.net', 'PERSONAL', now(), now());


INSERT INTO `contacts` (`cid`, `uid`, `name`, `lastname`, `picture`, `address`, `modification`, `creation`)
VALUES ('3', '1', 'Peter', 'Griffin', 'http://tinyurl.com/a39ukxn', 'Address Known', now(), now());

INSERT INTO `phones` (`cid`, `phone`, `type`, `modification`, `creation`)
VALUES ('3', '1234567890', 'MOBILE', now(), now());

INSERT INTO `phones` (`cid`, `phone`, `type`, `modification`, `creation`)
VALUES ('3', '1236587458', 'WORK', now(), now());

INSERT INTO `contact_sn` (`snid`, `cid`, `username`, `modification`, `creation`)
VALUES ('1', '3', 'petergriffin', now(), now());

INSERT INTO `emails` (`cid`, `email`, `type`, `modification`, `creation`)
VALUES ('3', 'peter@mail.net', 'PERSONAL', now(), now());