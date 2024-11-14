-- This query lists all shows from the hbtn_0d_tvshows database that have at least one genre linked
-- It displays the show title and the associated genre_id for each show
-- The results are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
