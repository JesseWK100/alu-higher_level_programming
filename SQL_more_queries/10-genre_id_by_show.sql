-- Select the title of the TV show and its associated genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
-- Join the tv_shows and tv_show_genres tables on the id field from tv_shows
-- and tv_show_id field from tv_show_genres
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.id
-- Order the results in ascending order by tv show title and genre ID
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
