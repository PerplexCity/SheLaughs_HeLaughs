from bs4 import BeautifulSoup
from urllib2 import urlopen
import time


#list of shows' wikipedia articles. This shows only five of the fifty
shows=['https://en.wikipedia.org/wiki/Master_of_None',
'https://en.wikipedia.org/wiki/Unbreakable_Kimmy_Schmidt',
'https://en.wikipedia.org/wiki/Manhattan_Love_Story',
'https://en.wikipedia.org/wiki/Broad_City',
'https://en.wikipedia.org/wiki/Mozart_in_the_Jungle'
]

showdic = {}
ratings = {}

#grabs IMDB links from Wikipedia article
for show in shows:

	time.sleep(2)

	#print show

	html = urlopen(show).read()
	soup = BeautifulSoup(html, "lxml")

	links = soup.findAll('a', href=True)
	for i in range(len(links)):
		if len(links[i].contents) >0:
			if links[i].contents[0] == 'Internet Movie Database':
				base = links[i-1]['href'][28:35]
				showdic[base] = [links[i-1]['href']+"ratings-male", links[i-1]['href']+"ratings-female"]
				print links[i-1]['href']+"ratings-male"


#grabs ratings just like other scripts
for key, value in showdic.items():
	
	#pauses to avoid scrutiny from IMDb
	time.sleep(5)
	
	try:
		html = urlopen(value[0]).read()
		soup = BeautifulSoup(html, "lxml")
		raw = [tr.find('td').text for tr in soup.findAll('tr')]
		Mvotes = sum(int(raw[i]) for i in range(1,11))
		Mpoints= sum(int(raw[i])*(11-i) for i in range(1,11))

		html = urlopen(value[1]).read()
		soup = BeautifulSoup(html, "lxml")
		raw = [tr.find('td').text for tr in soup.findAll('tr')]
		Fvotes = sum(int(raw[i]) for i in range(1,11))
		Fpoints= sum(int(raw[i])*(11-i) for i in range(1,11))

		ratings[key] = [Mvotes ,float(Mpoints)/Mvotes, Fvotes, 
		float(Fpoints)/Fvotes, float(Mpoints)/Mvotes-float(Fpoints)/Fvotes]

	except:
		#if it doesn't work for some reason, identifies the problematic show
		print value


#writes data file
writer = csv.writer(open('allshows.csv', 'wb'))
writer.writerow(["show", "mvotes", "maverage", "fvotes", "faverage", "difference"])

for key, value in ratings.items():
   writer.writerow([key, value])


