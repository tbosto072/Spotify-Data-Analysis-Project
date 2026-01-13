import pandas as pd
import numpy as np

data = pd.read_json("Streaming_History_Audio_2024-2025_2.json")
track_names = data['master_metadata_track_name']
artist_names = data['master_metadata_album_artist_name']

print(artist_names)