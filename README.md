# TheVoiceAnalytics

Simple collection of data mining scripts for the US edition of the show "The Voice". 

Written a few hours before the show's season finale to see who would be the most likely winner based on the number of sales they had obtained on iTunes. 

To use the scripts: 

- iTunesData.py collects all the itunes data from an external website by scanning and filtering a webapge 
- ContestantData.py scans a wiki page and filters the contestants critical info 
- ArtistDataTest and ArtistSales both search the results of the last two files for sales info 
- SalesVsWinner plots the winner and runner's up sales as a function of season number

The trend was quite clear, the artist who gets the most iTunes sales wins the show, with the exception of two out of 13 seasons. The winner 
was correctly predicted
