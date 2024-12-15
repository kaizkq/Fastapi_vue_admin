/*
 Navicat Premium Data Transfer

 Source Server         : mysql-master
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : demo

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 26/06/2024 22:19:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for books
-- ----------------------------
DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_0900_as_ci NOT NULL,
  `author` varchar(255) COLLATE utf8mb4_0900_as_ci NOT NULL,
  `published_date` date NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `category` varchar(255) COLLATE utf8mb4_0900_as_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_ci;

-- ----------------------------
-- Records of books
-- ----------------------------
BEGIN;
INSERT INTO `books` VALUES (1, '活着', '余华', '1994-06-07', '2024-06-26 15:03:29', '2024-06-26 22:08:42', '余华作品');
INSERT INTO `books` VALUES (2, '红楼梦', '曹雪芹', '2024-06-26', '2024-06-26 22:07:05', '2024-06-26 22:07:05', '古典文学');
INSERT INTO `books` VALUES (3, '三国演义', '罗贯中', '2024-06-26', '2024-06-26 06:09:40', '2024-06-26 14:10:08', '古典文学');
INSERT INTO `books` VALUES (5, '呐喊', '鲁迅', '2024-06-26', '2024-06-27 06:14:27', '2024-06-26 22:14:50', '鲁迅作品');
INSERT INTO `books` VALUES (6, '狂人日记', '鲁迅', '2024-06-26', '2024-06-26 14:15:32', '2024-06-26 14:15:32', '鲁迅作品');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8mb4_0900_as_ci DEFAULT NULL COMMENT '账号',
  `password` varchar(255) COLLATE utf8mb4_0900_as_ci DEFAULT NULL COMMENT '密码',
  `nickname` varchar(255) COLLATE utf8mb4_0900_as_ci DEFAULT NULL COMMENT '昵称',
  `avatar` varchar(255) COLLATE utf8mb4_0900_as_ci DEFAULT NULL COMMENT '头像url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_ci;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'ggbond', '$2b$12$2vJ8XUTZdTJ3cP1gzq4pWOj5Pu9uVvGioe/OxphMyWZQngsBg4B8m', NULL, NULL);
INSERT INTO `user` VALUES (2, 'admin', '$2b$12$3KwQrnPaL7/e3PEA6b0jHOLub7dHMWuhsSBrCxj9O6KX/rbgvMU0O', '萧嫣', NULL);
INSERT INTO `user` VALUES (3, 'kkk', '$2b$12$GcshM6Cl/BV.iC2nNrG0P.ctrqYMOB/FvBqEqGoxSdpVqIsWIUj3K', '猪猪', NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
