-- Select the genre and the count of shows linked to each genre
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
-- Join the tv_show_genres table with the tv_shows table
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
-- Group the results by genre
GROUP BY tv_show_genres.genre_id
-- Filter out genres with no linked shows
HAVING COUNT(tv_show_genres.tv_show_id) > 0
-- Sort the results in descending order by the number of shows linked
ORDER BY number_of_shows DESC;
