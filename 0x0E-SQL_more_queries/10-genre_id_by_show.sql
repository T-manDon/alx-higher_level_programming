-- this script lists shows in hbtn_0d_tvshows with at least one genre
   -- every record displays tv_shows.title - tv_show_genres.genre_id
   -- Results sorted in ascending order
   -- and tv_show_genres.genre_id
   -- The database name will pass as an arg of mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
