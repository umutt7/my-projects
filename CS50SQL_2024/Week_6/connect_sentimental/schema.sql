CREATE TABLE `users` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `first_name` VARCHAR(64) NOT NULL,
    `last_name` VARCHAR(64) NOT NULL,
    `username` VARCHAR(64) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

INSERT INTO `users` (`first_name`, `last_name`, `username`, `password`)
VALUES
('Claudine', 'Gay', 'claudine', 'password'),
('Reid', 'Hoffman', 'reid', 'password');


CREATE TABLE `schools` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(128) NOT NULL,
    `type` ENUM('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `location` VARCHAR(128) NOT NULL,
    `year` SMALLINT UNSIGNED,
    PRIMARY KEY(`id`)
);

INSERT INTO `schools` (`name`, `type`, `location`, `year`)
VALUES
('Harvard University', 'Higher Education', 'Cambridge, Massachusetts', 1636);


CREATE TABLE `companies` (
    `id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(64) NOT NULL,
    `industry` ENUM('Technology', 'Education', 'Business') NOT NULL,
    `location` VARCHAR(128) NOT NULL,
    PRIMARY KEY(`id`)
);

INSERT INTO `companies` (`name`, `industry`, `location`)
VALUES
('LinkedIn', 'Technology', 'Sunnyvale, California');


CREATE TABLE `follow` (
    `user_id` INT UNSIGNED,
    `follow_id` INT UNSIGNED,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`follow_id`) REFERENCES `users`(`id`)
);

CREATE TABLE `school_affiliates` (
    `user_id` INT UNSIGNED,
    `school_id` INT UNSIGNED,
    `start_date` DATE,
    `end_date` DATE,
    `type` VARCHAR(32),
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`)
);

INSERT INTO `school_affiliates` (`user_id`, `school_id`, `start_date`, `end_date`, `type`)
VALUES
(1, 1, '1993-01-01', '1998-12-31', 'PhD');


CREATE TABLE `company_affiliates` (
    `user_id` INT UNSIGNED,
    `company_id` INT UNSIGNED,
    `start_date` DATE,
    `end_date` DATE,
    FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`company_id`) REFERENCES `companies`(`id`)
);

INSERT INTO `company_affiliates` (`user_id`, `company_id`, `start_date`, `end_date`)
VALUES
(2, 1, '2003-01-01', '2007-02-01');
