-- lists genres in hbtn_0d_ and the linked shows
   -- Each should display
      -- <TV Show genre> - <Number of shows linked to this genre>
   -- Results sorted in descending order through the no. of linked shows
   -- database name will pass as argt of mysql command

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
