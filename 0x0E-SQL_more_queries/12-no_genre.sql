-- script lists the shows in hbtn_0d_tvshows without a linked genre
   -- Every record displays tv_shows.title - tv_show_genres.genre_id
   -- Results sorted in ascending order of tv_shows.title
   -- and tv_show_genres.genre_id
   -- The database name will pass as an argt of mysql command

SELECT title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
