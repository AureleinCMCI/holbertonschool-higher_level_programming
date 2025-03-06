
-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail


SELECT cities.id, cities.name 
FROM cities
WHERE cities.state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id;
