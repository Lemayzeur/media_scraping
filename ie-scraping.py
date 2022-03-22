import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs


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


url_list = ["https://lenouvelliste.com/","https://www.haitilibre.com/"]

keyWords = ["kidnapping","Kidnapping","kidnape","Kidnape","kidnaper","Kidnaper","Viol","viol","agression sexuelle","Agression sexuelle","Agressions sexuelles","agressions sexuelles",
"Fusillade","fusillade","Echange de tirs","echange de tirs","Coup de feu","coup de feu","Assassinat","assassinat","crime","Crime","meurtre","meurtres","Meurtre","Meurtres",
"Jovenel","Jovenel Moise","Martine","Martine Moise"]

if proxy:

	for site in url_list:
		res = requests.get(site, headers=headers, proxies=proxy) # TODO

		resContents = res.content

		#htmlContent = res.content

		print(resContents)

		# init the beautiful instance as html parser

		#soup = bs(resContents,'html.parser') # TODO
	
	
"""
	# After collecting the data needed, convert it to pandas dataframe
  # TODO

	# then export it as csv
	df.to_csv('<path/file_name>') # TODO
else:
	print('No working proxy found. Go buy some instead')

"""


