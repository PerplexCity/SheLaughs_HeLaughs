# She Laughs, He Laughs Loudest

The ratings for each individual episode are gathered using a web scraper that first updates the episode information using an IMDb Python package and then parses the data with Beautiful Soup. Thus, friends.py writes to the friends.csv file, and seinfeld.py writes to the seinfeld.csv file. 

The ratings for all the NYC sitcoms isn't as straightforward. I had to manually trim Wikipedia's list of NYC shows to the ones that counted (post-1990 sitcoms). I probably could have simply clicked the IMDb link from each individual Wikipedia page, since the total wasn't that many (~50), but I went ahead and wrote another scraper that grabbed the IMDb link from the Wikipedia article and then fed the links into the same ratings grabber from the Seinfeld and Friends scripts. Not super efficient or error-free, but allshows.csv was the result.

Once the datasets were ready/cleaned, some extra info was added (episode title for a select few, lead role gender for the all shows file), they were fed into the shows.R script to be visualized.

