
-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail


SELECT cities.id, cities.name, states.name 
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
 