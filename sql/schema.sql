-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `final` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `final` ;

-- -----------------------------------------------------
-- Table `final`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(18) NOT NULL,
  `email` VARCHAR(120) NOT NULL,
  `password` VARCHAR(60) NOT NULL,
  `fullname` VARCHAR(18) NOT NULL,
  `image_file` VARCHAR(20) NULL DEFAULT NULL,
  `biography` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `final`.`post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`post` (
  `post_id` INT NOT NULL AUTO_INCREMENT,
  `views` INT NOT NULL DEFAULT 0,
  `title` VARCHAR(100) NOT NULL,
  `content` TEXT NOT NULL,
  `file_path` VARCHAR(45) NULL DEFAULT NULL,
  `timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`post_id`),
  INDEX `fk_forum_post_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_forum_post_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `final`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`pet` (
  `pet_id` INT NOT NULL AUTO_INCREMENT,
  `species` VARCHAR(45) NOT NULL,
  `subspecies` VARCHAR(45) NULL DEFAULT NULL,
  `name` VARCHAR(18) NOT NULL,
  `color` VARCHAR(45) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `tagline` VARCHAR(150) NULL DEFAULT NULL,
  `image_file` VARCHAR(45) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `biography` TEXT NULL DEFAULT NULL,
  `img1_path` VARCHAR(45) NULL DEFAULT NULL,
  `img2_path` VARCHAR(45) NULL DEFAULT NULL,
  `img3_path` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`pet_id`),
  INDEX `fk_profile_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_profile_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `final`.`reply`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`reply` (
  `reply_id` INT NOT NULL AUTO_INCREMENT,
  -- `title` VARCHAR(100) NOT NULL,
  `content` TEXT NOT NULL,
  `timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,	
  `user_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  PRIMARY KEY (`reply_id`),
  INDEX `fk_reply_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reply_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION, 
  INDEX `fk_reply_forum_post_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_reply_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `final`.`post` (`post_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- -----------------------------------------------------
-- Table `final`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final`.`likes` (
  `user_id` INT NOT NULL,
  `reply_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `reply_id`),
  INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `final`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  INDEX `fk_reply_id_idx` (`reply_id` ASC) VISIBLE,
  CONSTRAINT `fk_reply_id`
    FOREIGN KEY (`reply_id`)
    REFERENCES `final`.`reply` (`reply_id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


ALTER TABLE user AUTO_INCREMENT=0;
ALTER TABLE pet AUTO_INCREMENT=0;
ALTER TABLE post AUTO_INCREMENT=0;
ALTER TABLE reply AUTO_INCREMENT=0;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
