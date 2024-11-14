-- Lists the genre names associated with the show "Dexter" in the hbtn_0d_tvshows database.
SELECT g.name
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN genres AS g ON tsg.genre_id = g.id
-- Filters to retrieve genres for the show with the title "Dexter."
WHERE ts.title = 'Dexter'
-- Sorts results by genre name in ascending order.
ORDER BY g.name ASC;

