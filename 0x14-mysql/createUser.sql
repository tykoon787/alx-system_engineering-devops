-- Script that creates a user 'holberton' with password
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT
ON *.*
TO 'holberton_user'@'localhost';