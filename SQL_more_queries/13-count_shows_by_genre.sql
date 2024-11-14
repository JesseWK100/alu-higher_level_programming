-- This query lists all genres from hbtn_0d_tvshows along with the number of shows linked to each genre.
-- It displays the genre and the number of shows, sorted in descending order by the number of shows linked.
-- Genres with no shows linked are excluded from the results.

SELECT genres.genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
