DROP TABLE IF EXISTS `jsondata`;
CREATE TABLE IF NOT EXISTS `jsondata` (
  `json_id` int(12) NOT NULL AUTO_INCREMENT,
  `gender` varchar(6) CHARACTER SET latin1 NOT NULL,
  `name` varchar(40) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`json_id`)
) ENGINE=MyISAM AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;