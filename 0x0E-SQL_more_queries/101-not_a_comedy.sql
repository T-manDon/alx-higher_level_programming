-- this script lists shows without genre Comedy in dtbase hbtn_0d_tvshows
   -- Each record displays
      -- tv_shows.title
   -- Results sorted in ascending order using show title
   -- database name passed as an argment of the mysqlnd

SELECT tv_shows.title FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
      JOIN tv_genres ON tv_genres.id=tv_show_genres.genre_id
      WHERE tv_genres.name = "Comedy" )
ORDER BY tv_shows.title;
