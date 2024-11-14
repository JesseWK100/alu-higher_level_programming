-- Select the genre names for the show titled 'Dexter'
SELECT genres.name
-- Join the tv_shows and tv_show_genres tables
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
-- Filter the results to include only the show titled 'Dexter'
WHERE tv_shows.title = 'Dexter'
-- Sort the results in ascending order by the genre name
ORDER BY genres.name ASC;
