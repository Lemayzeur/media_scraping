import csv
from datetime import datetime
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs

scheme = 'https'
target_host = 'lenouvelliste.com/national '
target_url = f'{scheme}://{target_host}'
print(target_url)
proxy_url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'


#header
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
}
# get the proxy as http response
# TODO

# Convert the http response to list of proxy
# TODO

def get_random_proxy(proxy_list):
	''' get a random proxy '''
	proxy = random.choice(proxy_list)
	return{
		'http' : proxy,
	}

	# to get more info on the proxy format
	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
	return # {'protocol': 'ip:port'} # TODO

def get_working_proxy():
	''' test random proxies, to get one that works'''
	response = requests.get(proxy_url)
	proxy_list = response.text.strip().split('\n')
 
	TOTAL_TESTS = 20
	print('Proxy works, good Job!')
	for _ in range(TOTAL_TESTS):
		proxy = get_random_proxy(proxy_list) # TODO
		print('%s) Trying proxy %s' %(_ + 1, proxy))
 
		try:
			response = requests.get('https://www.google.com/', proxies=proxy, timeout = 10) # TODO
			# if it works, return it
			if response.status_code == 200:
				print('One proxy found %s' %proxy)
				return proxy
		except: 
			print('Not good\n')
	print(f'We have tried {TOTAL_TESTS} time(s), but no working proxy found')
 
proxy = get_working_proxy()
#dataset
data = []
words = ['Kidnapping', 'Kidnaping', 'Kidnapé', 'Kidnapper', 'Viol', 'agression sexuelle',
 'Fusillade', 'échange de tir', 'coup de feu', 
 'Assassinat', 'homicide', 'crime', 'meurtre', 
 'Jovenel', 'Jovenel Moise', 'Jovenel Moïse',' Martine Moïse', 
]

if proxy:

	# hit the target site
	try:
		print('Querying %s...' % target_url)
		pageNum = 1
		while pageNum <= 2585:
      
			response = requests.get(f"https://lenouvelliste.com/national?page={pageNum}",headers=header, proxies = proxy) # TODO
			# response.encoding = response.apparent_encoding
			if response.status_code == 200:
				print('Status code is: 200')
				soupB = bs(response.text, 'html.parser')
    
				divList = soupB.find_all('div', {'class':'content_widget'})
				# print(divList)
				# for div in divList:
				# 	titre_liste = div.find('h2')
				# 	for titre in titre_liste:
				# 		titre_liste.append(titre.string)
				# 		titre1 = titre_liste
				# 	print(titre1)
     
				for div in divList:
					lien = div.find("a")["href"]

					content = requests.get(lien)
					soupC = bs(content.text, "html.parser")
					
					head = ["article", 'Url']
					with open('ie_scraping.csv','w') as ie_scraping_csv:
						writer = csv.writer(ie_scraping_csv, delimiter =',')
						writer.writerow(head)

					tit = soupC.find('h2').text.strip()
					dat = soupC.find('small').text.strip()
					kontni = soupC.find('article').text.strip()

     
					data.append(
								{
									'Article': tit,
									'Url': lien,
									'dat': dat,
									# 'kontni': kontni
								}
							)
			else: print('Request failed with status code', response.status_code)
   
			pageNum += 1
			print(f"Search Page ={pageNum}", " - END")
			print('Will go to the next page!')

		#convert datalist to csv file with pandas
		dataf = pd.DataFrame(data)
		dataf.to_csv('ie_scraping.csv')

	except Exception as err: print('Request failed', err)