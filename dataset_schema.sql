-- -----------------------------------------------------
-- Table `topic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `topic` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` LONGTEXT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `links`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `links` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `link` LONGTEXT NULL,
  `topic_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `topic_id_idx` (`topic_id` ASC) VISIBLE,
  CONSTRAINT `topic_id`
    FOREIGN KEY (`topic_id`)
    REFERENCES `topic` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `content` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` LONGTEXT NULL,
  `content` LONGTEXT NULL,
  `link_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `link_id_idx` (`link_id` ASC) VISIBLE,
  CONSTRAINT `link_id`
    FOREIGN KEY (`link_id`)
    REFERENCES `links` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
