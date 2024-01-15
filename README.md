# LastfmListens
This is a project to visualize my music listening history, as logged on Last.fm to draw insights on my listening habits such as top plays by year, artist and even genre.

This involved getting data using the Last.fm API, using 2 end points:
* user.getRecentTracks - to get my lisening history, ordered by recency
* track.getTopTags - To get the top 3 tags of each track

The data from these were gotten in JSON format, which were then put into data frames, cleaned by dropping columns that were not needed, such as the 'mbid' column and formatting columns such as the date column

This data frame was then exported to tableau to create a summary visualization of my music listens, which can be filtered for a certain year or all time stats.
The interactive dashboard can be viewed [here](https://public.tableau.com/app/profile/ewaoluwa.osunrayi/viz/EwasMusicStatistics2/WHOWHATWHEN)
![WHO_ WHAT_ WHEN](https://github.com/EwaoluwaO/LastfmListens/assets/107421136/313a2bf2-9097-4c5b-98b2-4abf35d32a6f)
