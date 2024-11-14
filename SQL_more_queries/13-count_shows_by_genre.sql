-- This query lists all genres from hbtn_0d_tvshows along with the number of shows linked to each genre.
-- It displays the genre and the number of shows, sorted in descending order by the number of shows linked.
-- Genres with no shows linked are excluded from the results.

SELECT tv_show_genres.genre_id, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
