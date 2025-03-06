-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail
   
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
