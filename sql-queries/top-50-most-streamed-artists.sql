--SQL query that lists my top 50 most streamed artists

SELECT artist_name, SUM(ms_played) AS total_ms_streamed
FROM spotify_db_updated
GROUP BY artist_name
ORDER BY SUM(ms_played) DESC
LIMIT 50;