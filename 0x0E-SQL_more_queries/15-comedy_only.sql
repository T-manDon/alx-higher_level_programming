-- the script lists comedy shows in database hbtn_0d_tvshows
-- displays no. of shows linked to each
   -- Each record displays
      -- tv_shows.title
   -- Results sorted in ascending order by the show title
   -- The database name will pass as an argment of mysql

SELECT title FROM tv_shows
JOIN tv_show_genres ON id=tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
