# She Laughs, He Laughs Loudest

The ratings for each individual episode are gathered using a web scraper that first updates the episode information using an IMDb Python package and then parses the data with Beautiful Soup. Thus, friends.py writes to the friends.csv file, and seinfeld.py writes to the seinfeld.csv file. 

One thing to note for all these ratings is that the "average" that IMDb prints was not used because it is a "Bayesian Average," which means that IMDb attaches a weight to it first to balance out episodes that have few ratings and are therefore vulnerable to extreme reviews. It's a strategy that most rating aggregator sites use. However, since IMDb doesn't tell us their formula, and since they only rate to a single decimal place, we will reconstruct the true averages by summing up the 1s, 2s, ... 9s, and 10s. 

The ratings for all the NYC sitcoms isn't as straightforward. I had to manually trim Wikipedia's list of NYC shows to the ones that counted (post-1990 sitcoms). I probably could have simply clicked the IMDb link from each individual Wikipedia page, since the total wasn't that many (~50), but I went ahead and wrote another scraper that grabbed the IMDb link from the Wikipedia article and then fed the links into the same ratings grabber from the Seinfeld and Friends scripts. Not super efficient or error-free, but allshows.csv was the result.

Once the datasets were ready/cleaned, some extra info was added (episode title for a select few, lead role gender for the all shows file), they were fed into the shows.R script to be visualized.

