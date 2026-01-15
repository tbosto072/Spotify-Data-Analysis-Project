import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Read CSV file
df = pd.read_csv('condensed.csv')

#Connect to local sqlite database
conn = sqlite3.connect('spotify.sqlite')

#Query that selects artist names as well as the frequency of each artist name
#that appears in the database. Limits query to the first 25 artists
query = """
SELECT artist_name, COUNT(artist_name) AS stream_count
FROM spotify_db
GROUP BY artist_name
ORDER BY COUNT(artist_name) DESC
LIMIT 25;
"""

#Read SQL query into a DataFrame
df = pd.read_sql_query(query, conn)

# Remove rows with None/null artist names to ensure matplotlib functionality
df = df.dropna(subset=['artist_name'])

#Bar graph setup
plt.bar(df['artist_name'], df['stream_count'])
plt.xlabel('Artist')
plt.ylabel('Stream Count')
plt.title('Artist Stream Counts')
plt.show()

conn.close()