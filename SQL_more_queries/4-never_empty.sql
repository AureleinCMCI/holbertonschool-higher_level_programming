-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
