import requests
import random
import csv
from bs4 import BeautifulSoup as bs
import re


#Url for the list of proxy

free_proxy_url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt' # TODO

# get the proxy as http response
# TODO

response_proxy = requests.get(free_proxy_url)

# Convert the http response to list of proxy
# TODO
proxy_list = response_proxy.text.strip().split("\n")


#print(proxy_list)



def get_random_proxy(array):
	''' get a random proxy '''
	proxy = random.choice(array)

	# to get more info on the proxy format
	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests

	return{
	'http':proxy,


	} # {'protocol': 'ip:port'} # TODO

def get_working_proxy():
	''' test random proxies, to get one that works'''
	TOTAL_TESTS = 20
	for i in range(TOTAL_TESTS):
		proxy = get_random_proxy(proxy_list) # TODO
		try:
			requests.get('https://www.google.com/', proxies=proxy) # TODO
			# if it works, return it

			return proxy
		except Exception as error:
			print(error)



# set a custom header

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0' # TODO
}

# call and get the proxy
proxy = get_working_proxy()

#Test
#print(proxy)


#url_leNouvelliste = "https://lenouvelliste.com/national?"



#"https://www.haitilibre.com/"

keyWords = ["kidnapping","Kidnapping","séquestration","Séquestration","rançon","Rançon","kidnapé","Kidnapé","kidnaper","Kidnapée","kidnapée","Kidnaper","Viol","viol","agression sexuelle","Agression sexuelle","Agressions sexuelles","agressions sexuelles",
"Fusillade","fusillade","Echange de tirs","échange de tirs","Coup de feu","coup de feu","Assassinat","assassinat","Assassiné","assassineé","Assassinée","assassinée","Assassiner","assassiner","crime","Crime","meurtre",
"meurtres","Meurtre","Meurtres","Jovenel","Jovenel Moise","Jovenel Moïse","Martine","Martine Moise","Martine Moïse","assassin"]

Articles = []
url = []


if proxy:

	for i in range(1,2585):

	
		resNouv = requests.get("https://lenouvelliste.com/national?page={0}".format(i), headers=headers, proxies=proxy) # TODO

		NouvellisteContents = resNouv.content

		#print(NouvellisteContents)


	
		soup = bs(NouvellisteContents,'html.parser')

		divNouvArticles = soup.find_all("div", {"class" : "content_widget"})

		for div in divNouvArticles:

			titleNouvArticles = div.find("h2")

			for title in titleNouvArticles:
				for word in keyWords:
					if word in title.string:
						Articles.append(title.string)
						url.append(title)


						
header = ["Articles","Url"]

with open('dataInfo.csv','w') as dataInfo_csv:

	writer = csv.writer(dataInfo_csv,delimiter=',')

	writer.writerow(header)


	for article,url in zip(Articles,url):
		row = [article,url]
		writer.writerow(row)
				
				






















		
		

		

		
"""
	
	else:
	print('No working proxy found. Go buy some instead')

"""


