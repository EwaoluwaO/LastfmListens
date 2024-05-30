# LastfmListens
## Project Overview

This project aims to visualize music listening history from Last.fm, uncovering intriguing insights about personal listening habits. It utilizes Python for data retrieval and cleaning, and Tableau for crafting interactive visualizations.

The data is processed using an Extract, Transform, Load (ETL) procedure:

* Extract: Read existing data from a CSV file and identify new listens by comparing them to the most recent date.
* Transform: Process and clean the new data.
* Load: Update the CSV file with the new information.

This ETL process is automated to run daily using Apache Airflow by scheduling a Directed Acyclic Graph (DAG).

## Key Features:

Visualize top artists, tracks, and genres by year or all-time.
Discover listening patterns over time, including seasonal trends.

## Technical Details

Languages and Libraries:

Python

* requests: API calls
* pandas: data wrangling
Tableau: data visualization

API Endpoints:

Last.fm API
  * user.getRecentTracks: retrieves listening history
  * track.getTopTags: fetches top tags for each track

Data Processing:

* Retrieve JSON data from Last.fm API endpoints.
* Create pandas DataFrames for efficient data manipulation.
* Clean and format data, including:
  * Dropping unnecessary columns (e.g., mbid)
  * Formatting date columns
  * Resolving potential data inconsistencies
* Export DataFrame to Tableau for visualization.

This data frame was then exported to tableau to create a summary visualization of my music listens, which can be filtered for a certain year or all time stats.
The interactive dashboard can be viewed [here](https://public.tableau.com/app/profile/ewaoluwa.osunrayi/viz/EwasMusicStatistics2/WHOWHATWHEN)
![WHO_ WHAT_ WHEN](https://github.com/EwaoluwaO/LastfmListens/assets/107421136/313a2bf2-9097-4c5b-98b2-4abf35d32a6f)
