-- Select the genre and the count of shows linked to each genre
SELECT genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
-- Join the tv_show_genres table with the genres table
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
-- Group the results by genre
GROUP BY genres.name
-- Filter out genres with no linked shows
HAVING COUNT(tv_show_genres.genre_id) > 0
-- Sort the results in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
