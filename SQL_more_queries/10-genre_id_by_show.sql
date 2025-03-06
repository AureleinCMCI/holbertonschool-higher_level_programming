
-- creates the MySQL server user user_0d_1.
   -- user_0d_1 should have all privileges on your MySQL server
   -- password set to user_0d_1_pwd
   -- If the user user_0d_1 already exists, script should not fail

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
