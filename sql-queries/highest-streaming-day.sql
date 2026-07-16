--SQL query that finds the day where I listened to the most music

SELECT date_listened, ms_played
FROM spotify_db_updated
GROUP BY date_listened
ORDER BY ms_played DESC;