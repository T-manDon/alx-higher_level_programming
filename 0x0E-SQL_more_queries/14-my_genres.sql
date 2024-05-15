-- script lists genres of the dexter show.
   -- Each record displays the:
      -- tv_genres.name
   -- Results sorted in ascending order through genre name
   -- The database name will pass as an argnt of the mysql

SELECT name FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
