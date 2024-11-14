-- Select the genre name and the count of shows linked to each genre
SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
-- Join the tv_show_genres table with the genres table
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
-- Group the results by genre name
GROUP BY genres.name
-- Filter out genres with no linked shows
HAVING COUNT(tv_show_genres.tv_show_id) > 0
-- Sort the results in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
