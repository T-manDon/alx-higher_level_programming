-- script lists shows and linked genres from database hbtn_0d_tvshows
   -- If a show lacks a genre, display NULL in its column
   -- Each record displays
      -- tv_shows.title - tv_genres.name
   -- Results sorted in ascending order using show title and genre
   -- The database name will pass as an argment of mysql command

SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
