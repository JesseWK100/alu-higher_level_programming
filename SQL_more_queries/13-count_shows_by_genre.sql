-- Selects the genre name and counts the number of shows linked to each genre.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
-- Joins the tv_show_genres table with genres to get genre names for each genre_id.
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
-- Groups the results by genre name to get a count for each genre.
GROUP BY genres.name
-- Ensures only genres with shows linked are displayed.
HAVING number_of_shows > 0
-- Orders the results in descending order by the number of shows linked.
ORDER BY number_of_shows DESC;
