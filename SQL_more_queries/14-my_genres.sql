-- Selects the genre name of all genres linked to the show "Dexter".
SELECT genres.name
-- Joins the tv_shows and tv_show_genres tables to get the genres for the show.
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
-- Filters to get only the show titled "Dexter".
WHERE tv_shows.title = 'Dexter'
-- Orders the results in ascending order by genre name.
ORDER BY genres.name ASC;
