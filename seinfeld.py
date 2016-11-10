from imdb import IMDb
from bs4 import BeautifulSoup
from urllib2 import urlopen
import time 
import csv

ia = IMDb()

#updates general Seinfeld file
Seinfeld = ia.get_movie('0108778')
ia.update(Seinfeld, 'episodes')

seinseasons={}

#updates each episode number
for i in Seinfeld['episodes']:
	if i>0:
		epis = []
		for j in Seinfeld['episodes'][i]:
			epi = (Seinfeld['episodes'][i][j])
			ia.update(epi)
			epis.append(ia.get_imdbID(epi))
		seinseasons[i] = epis

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
for key, value in seinseasons.items():
	for i in value:
		print i
		#pauses for five seconds to avoid getting banned by IMDb...
		time.sleep(5)
		maleURL = "http://www.imdb.com/title/tt" + str(i) +"/ratings-male"
		femaleURL = "http://www.imdb.com/title/tt" + str(i) +"/ratings-female"
		mrating = grabvotes(maleURL)
		frating = grabvotes(femaleURL)
		ratings[i]= [mrating, frating, round(mrating-frating,2)]

#writes data file
writer = csv.writer(open('sein2.csv', 'wb'))
writer.writerow(["episode", "men", "women", "difference"])

for key, value in ratings.items():
   writer.writerow([key, value])

