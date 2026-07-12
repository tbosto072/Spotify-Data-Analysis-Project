import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import json

#Read Spotify JSON data file
data = pd.read_json("Streaming_History_Audio_2024-2025_2.json")

#Create DataFrame series for each column that I want to use from JSON file
track_names = data['master_metadata_track_name']
artist_names = data['master_metadata_album_artist_name']
album_names = data['master_metadata_album_album_name']

#Take substring of 'ts' column of JSON file to create shortened date from timestamp
data['date_listened'] = data['ts'].str[0:10] 

#Create condensed DataFrame from columns selected above
df_condensed = data[['master_metadata_track_name', 'master_metadata_album_album_name', 'master_metadata_album_artist_name', 'ms_played', 'date_listened', 'platform']]

#Rename columns for readability
df_condensed.columns = ['track_name', 'album_name', 'artist_name', 'ms_played', 'date_listened', 'platform']

#Clean any null data
df_condensed.dropna(inplace=True)

#Filter and remove any song data where ms_played is below 50 seconds to ensure skipped songs are deleted
df_condensed = df_condensed.loc[df_condensed['ms_played'] > 50000]

#Convert condensed DataFrame to CSV file
df_condensed.to_csv('condensed_v2.csv', index=False)

#Function to convert CSV file into SQLite table
def csv_to_sqlite():
    try:
        df = pd.read_csv('condensed_v2.csv')
        conn = sqlite3.connect('spotify.sqlite')
        df.to_sql('spotify_db_updated', conn, if_exists='replace',index=False)
        conn.commit()
        conn.close()
        print(f"Successfully converted csv file to sql")
    except Exception as e:
        print(f"An error occurred: {e}")

#Run conversion
csv_to_sqlite()
        