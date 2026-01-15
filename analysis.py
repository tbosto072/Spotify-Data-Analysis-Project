import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import json

#Read Spotify JSON data file
data = pd.read_json("Streaming_History_Audio_2024-2025_2.json")

#Create series for each column that I want to use from JSON file
track_names = data['master_metadata_track_name']
artist_names = data['master_metadata_album_artist_name']
album_names = data['master_metadata_album_album_name']

#Create condensed DataFrame from columns selected above
df_condensed = data[['master_metadata_track_name', 'master_metadata_album_album_name', 'master_metadata_album_artist_name', 'ms_played']]

#Rename columns
df_condensed.columns = ['track_name', 'album_name', 'artist_name', 'ms_played']

#Convert condensed DataFrame to CSV file
df_condensed.to_csv('condensed.csv', index=False)

#Function to converty CSV file into SQLite table
def csv_to_sqlite():
    try:
        df = pd.read_csv('condensed.csv')
        conn = sqlite3.connect('spotify.sqlite')
        df.to_sql('spotify_db', conn, if_exists='replace',index=False)
        conn.commit()
        conn.close()
        print(f"Successfully converted csv file to sql")
    except Exception as e:
        print(f"An error occurred: {e}")

#Run conversion
csv_to_sqlite()
        