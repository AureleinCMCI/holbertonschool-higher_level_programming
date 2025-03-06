
-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail



CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
       name VARCHAR(256) NOT NULL);