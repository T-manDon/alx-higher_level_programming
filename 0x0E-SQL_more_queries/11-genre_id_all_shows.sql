-- script lists all shows in dtbase hbtn_0d_tvshows
   -- every record display tv_shows.title - tv_show_genres.genre_id
   -- Results sorted in ascending order through tv_shows.title
   -- and tv_show_genres.genre_id
   -- If a tv show lacks a genre, display NULL
   -- The database name passes as an argt of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
