-- Script that creates the replica_user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON tyrell_corp.* TO 'replica_user'@'%';
GRANT INSERT, UPDATE, DELETE ON tyrell_corp.* TO 'replica_user'@'%';
FLUSH PRIVILEGES;