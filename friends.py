from imdb import IMDb
from bs4 import BeautifulSoup
from urllib2 import urlopen
import time 
import csv

ia = IMDb()

Friends = ia.get_movie('0108778')
ia.update(Friends, 'episodes') #updates general Friends file

friendsseasons={}

for i in Friends['episodes']: #updates each episode number
	if i>0:
		epis = []
		for j in Friends['episodes'][i]:
			epi = (Friends['episodes'][i][j])
			ia.update(epi)
			epis.append(ia.get_imdbID(epi))
		friendsseasons[i] = epis

ratings = {}


#IMDb scraper
def grabvotes(url):

	html = urlopen(url).read()
	soup = BeautifulSoup(html, "lxml")
	raw = [tr.find('td').text for tr in soup.findAll('tr')]
	points= sum(int(raw[i])*(11-i) for i in range(1,11))
	votes = sum(int(raw[i]) for i in range(1,11))

	return round(float(points)/votes,2)

#grabs male and female ratings from each
for key, value in friendsseasons.items():
	for i in value:
		print i
		time.sleep(5)
		maleURL = "http://www.imdb.com/title/tt" + str(i) +"/ratings-male"
		femaleURL = "http://www.imdb.com/title/tt" + str(i) +"/ratings-female"
		mrating = grabvotes(maleURL)
		frating = grabvotes(femaleURL)
		ratings[i]= [mrating, frating, mrating-frating]

#writes data file
writer = csv.writer(open('friends.csv', 'wb'))
writer.writerow(["episode", "men", "women", "difference"])

for key, value in ratings.items():
   writer.writerow([key, value])

