# Spotify Data Analysis Project

A comprehensive data analysis project that processes personal Spotify streaming history to generate insights and visualizations. This project demonstrates proficiency in Python, SQL, data cleaning, and data visualization.

## Project Overview

This project analyzes Spotify listening history data by:
- Extracting and cleaning data from Spotify's exported JSON files
- Converting and storing data in SQLite for efficient querying
- Generating statistical summaries and visualizations
- Identifying top artists and streaming patterns

## Features

- **Data Processing**: Extracts relevant fields from Spotify JSON exports (track name, artist, album, listening duration)
- **Data Persistence**: Converts cleaned data to both CSV and SQLite database formats
- **Analytics**: Aggregates streaming data by artist with frequency counts
- **Visualization**: Creates bar charts showing top artists by stream count
- **Error Handling**: Robust null value handling and data validation

## Project Structure

```
├── analysis.py                          # Data extraction and SQLite conversion
├── plots.py                             # Visualization generation
├── condensed.csv                        # Processed Spotify data (CSV format)
├── spotify.sqlite                       # SQLite database with spotify_db table
├── Streaming_History_Audio_2024-2025_2.json  # Raw Spotify export data
└── README.md                            # Project documentation
```

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

### Step 1: Run Data Analysis
```bash
python analysis.py
```
This script:
- Reads the Spotify JSON export file
- Extracts track name, album, artist, and listening duration
- Creates a condensed CSV file (`condensed.csv`)
- Converts the CSV to SQLite database format (`spotify.sqlite`)

### Step 2: Generate Visualizations
```bash
python plots.py
```
This script:
- Queries the SQLite database for top 25 artists
- Aggregates stream counts by artist
- Removes null values to ensure data integrity
- Displays an interactive bar chart showing artist stream frequencies

## Data Schema

### spotify_db Table
| Column | Type | Description |
|--------|------|-------------|
| track_name | TEXT | Name of the track |
| album_name | TEXT | Album containing the track |
| artist_name | TEXT | Primary artist name |
| ms_played | INTEGER | Milliseconds the track was played |

## Key Insights

The analysis provides:
- **Top Artists**: Identifies your most-streamed artists by frequency
- **Stream Distribution**: Visualizes how your listening is distributed across artists
- **Listening Patterns**: Data can be extended to analyze temporal trends and preferences

## Technical Stack

- **Language**: Python 3.x
- **Data Processing**: pandas
- **Visualization**: matplotlib
- **Database**: SQLite3
- **Data Format**: JSON, CSV

## Future Enhancements

Potential extensions for this project:
- Time-series analysis of listening patterns over months/years
- Genre classification and distribution analysis
- User interaction dashboard with plotly/dash
- Statistical analysis of listening duration patterns
- Export analysis results to interactive HTML reports
- Playlist recommendation engine based on listening history

## Notes

- The project handles null/missing artist names gracefully by filtering them during visualization
- SQLite database is recreated each time `analysis.py` runs, ensuring fresh data
- Bar chart displays limited to top 25 artists for clarity and readability
