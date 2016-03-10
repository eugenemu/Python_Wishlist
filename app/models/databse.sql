-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema itemsdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema itemsdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `itemsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `itemsdb` ;

-- -----------------------------------------------------
-- Table `itemsdb`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `itemsdb`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `name` VARCHAR(255) NULL COMMENT '',
  `username` VARCHAR(255) NULL COMMENT '',
  `pw_hash` VARCHAR(255) NULL COMMENT '',
  `date_hired` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `username_UNIQUE` (`username` ASC)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `itemsdb`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `itemsdb`.`items` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `item` VARCHAR(255) NULL COMMENT '',
  `created_at` DATETIME NULL COMMENT '',
  `user_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_items_users1_idx` (`user_id` ASC)  COMMENT '',
  CONSTRAINT `fk_items_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `itemsdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `itemsdb`.`wishlist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `itemsdb`.`wishlist` (
  `item_id` INT NOT NULL COMMENT '',
  `user_id` INT NOT NULL COMMENT '',
  PRIMARY KEY (`item_id`, `user_id`)  COMMENT '',
  INDEX `fk_items_has_users_users1_idx` (`user_id` ASC)  COMMENT '',
  INDEX `fk_items_has_users_items_idx` (`item_id` ASC)  COMMENT '',
  CONSTRAINT `fk_items_has_users_items`
    FOREIGN KEY (`item_id`)
    REFERENCES `itemsdb`.`items` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_items_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `itemsdb`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
