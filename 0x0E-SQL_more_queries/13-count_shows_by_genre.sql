-- list all genres and number of shows linked to it
-- Script that lists all genres from hbtn_0d_tvshows
-- Displays number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
