--SQL query that ranks songs from each Beyoncé album by stream count
--Ranks each track in each album by stream count using dense_rank()
--Top streamed songs are ranked highest, lowest streamed songs ranked lowest

SELECT artist_name, track_name, album_name, COUNT(track_name) AS stream_count, dense_rank() OVER(PARTITION BY album_name ORDER BY COUNT(track_name) DESC)  AS rank
FROM spotify_db_updated
WHERE artist_name = 'Beyoncé'
GROUP BY track_name;