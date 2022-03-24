from attr import attr
import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs

free_proxy_url = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt' # TODO

# get the proxy as http response
# TODO
r = requests.get(free_proxy_url)
# Convert the http response to list of proxy
# TODO
soup = bs(r.text, "html.parser").find_all("td", {"class": "blob-code blob-code-inner js-file-line"})

proxy = [proxy.text for proxy in soup]

def get_random_proxy(array):
	''' get a random proxy '''
	proxy = random.choice(array)

	# to get more info on the proxy format
	# More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
	return {'http': proxy}

def get_working_proxy():
	''' test random proxies, to get one that works'''
	TOTAL_TESTS = 20
	for _ in range(TOTAL_TESTS):
		prox = get_random_proxy(proxy) # TODO
		try:
			requests.get('https://www.google.com/', proxies=prox) # TODO
			# if it works, return it
			return prox
		except Exception as error:
			print(error)
# call and get the proxy
# p = get_working_proxy()
# print(p)

# set a custom header
headers = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1' # TODO
}

nombres_pages = 1
# res = requests.get('https://lenouvelliste.com/national?page=1', headers=headers, proxies=p) # TODO
# print(res.text)
for page in range(0,nombres_pages):
	if proxy:
		prox = get_working_proxy()
		res = requests.get('https://lenouvelliste.com/national?page='+str(page+1), headers=headers, proxies=prox) # TODO
		# print(res.text)
        
		soup = bs(res.text, 'html.parser') 
        
        
		lien = soup.find_all('a', attrs={'class':'mrf-buttonOpacityLight mrf-button mrf-buttonArticle mrf-hidden-link'})
		lien = [link.get('href') for link in lien]
		filename="NEWS.csv"
		f=open(filename,"w", encoding = 'utf-8')
		entete="Article, url, date, KNPG_M, TM_KNPG, V_M, TM_V, FSD_M, TM_FSD, ASST_M, TM_ASST, JVL_M TM_JVL\n"
		f.write(entete)
 
		for i in lien:
			res = requests.get(i)
			soup = bs(res.text, 'html.parser') 
			article = soup.find('div', {'class':'detail_content_area'}).find('h2').text
			url = soup.find('div', {'class':'auteur_right pull-right'}).find('a')['href']
			print(article)
			
			
					
		# init the beautiful instance as html parser
		# soup = bs(res , 'html.parser') # TODO
  
        
	# After collecting the data needed, convert it to pandas dataframe
  # TODO

	# then export it as csv
	# df.to_csv('<path/file_name>') # TODO
# else:
# 	print('No working proxy found. Go buy some instead')
