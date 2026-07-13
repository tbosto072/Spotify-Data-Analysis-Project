# Spotify Listening History Data Analysis Project

A comprehensive data analysis project that processes my personal Spotify streaming history to generate insights and visualizations. This project demonstrates proficiency in Python by utilizing Pandas, writing SQL queries, data cleaning, data pipeline creation, and data visualization.

## Project Overview

I analyzed my data by doing the following:
- Extracted and transformed raw data from Spotify's exported JSON files into a CSV file
- Cleaned and removed null and irrelevant data
- Converted and stored data in a SQLite database for efficient querying
- Identified top artists and streaming patterns with SQL queries that used aggregations and window functions
- Created visualization dashboard with PowerBI

## Project Structure

```
├── README.md                            # Project documentation
├── Spotify Analysis Dashboard.png       # Image of my public Tableau dashboard
├── Spotify Analysis PowerBI Report.pdf  # PDF of PowerBI dashboard
├── Spotify PowerBI Dashboard.png        # Image of my PowerBI dashboard for readme
├── Streaming_History_Audio_2024-2025_2.json  # Raw Spotify export data
├── analysis.py                          # Python scripts for data pipeline
├── condensed.csv                        # Processed Spotify data (CSV format)
├── condensed_v2.csv                     # Updated CSV file to include date and platform (7/11/2026)
├── spotify.sqlite                       # SQLite database with spotify_db table
└── spotify_db                           # SQLite table with schema
```

## PowerBI Dashboard
- This dashboard contains charts that display my top 10 artists, songs and albums, as well as other insights like hourly listening trends and platform usage.
  
![Image of PowerBI Dashboard](https://github.com/tbosto072/Spotify-Data-Analysis-Project/blob/main/Spotify%20PowerBI%20Dashboard.png)

## Key Insights
- **Top Streamed Artist**: Beyoncé
- **Favorite Platform**: ios (iPhone/iPad)
- **Top Streamed Month**: March 2025 | 172,000,000 ms = 47 Hours
- **Least Streamed Month**: December 2024 | 98,000,000 ms = 27 hours
- **Listening Behavior**: Beyoncé streaming numbers skyrocketed in February 2025 due to her announcing her Cowboy Carter Tour, and in July 2025 due to that being my birthday month where I was going to see her in concert.

## Prerequisites

- Python 3.7 or higher
- Required packages:
  - pandas
  - matplotlib
  - numpy
  - sqlite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tbosto072/Spotify-Data-Analysis-Project.git
cd Spotify-Data-Analysis-Project
```

2. Install required dependencies:
```bash
pip install pandas matplotlib numpy
```

3. Obtain your Spotify data:
   - Go to https://www.spotify.com/us/account/privacy/
   - Request your personal data
   - Download the JSON files containing your streaming history

## Usage

### Step 1: Run Data Pipeline
```bash
python analysis.py
```
This script:
- Reads the Spotify JSON export file
- Extracts track name, album, artist, listening duration, date listened, and platform
- Creates a condensed CSV file (`condensed_v2.csv`)
- Converts the CSV to SQLite database format (`spotify.sqlite`)


## Data Schema

### spotify_db Table
| Column | Type | Description |
|--------|------|-------------|
| track_name | TEXT | Name of the track |
| album_name | TEXT | Album containing the track |
| artist_name | TEXT | Primary artist name |
| ms_played | INTEGER | Milliseconds the track was played |
| date_listened | TEXT | Date the track was played |
| platform | TEXT | Platform the track was played on|

