-- Script that creates a table 'tyrell_corp'
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6  (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL
);
INSERT INTO nexus6 (id,  name) VALUES (1, 'Leon');