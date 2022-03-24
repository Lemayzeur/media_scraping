import re
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

def count_words(url, liste):
    n = 0
    for word in liste:
        r = requests.get(url, allow_redirects=False)
        soup = bs(r.content, 'html.parser')
        words = ''.join([t for t in soup.body.article.find_all(text=True)])
        words = words.lower()
        words = words.split()
        nb = words.count(word.lower())
        n = n + nb
    if n == 0:
        global bol
        bol = False
    else:
        bol = True
    return n

# def bool_check(url, liste):
#     nb = count_words(liste)
#     if nb == 0:
#        return False
#     else:
#         return True    
    
nombres_pages = 2					
# res = requests.get('https://lenouvelliste.com/national?page=1', headers=headers, proxies=p) # TODO
# print(res.text)
upperframe=[]  
for page in range(0,nombres_pages):
	if proxy:
		prox = get_working_proxy()
		res = requests.get('https://www.haitilibre.com/flash-infos-'+str(page+1), headers=headers, proxies=prox) # TODO
		# print(res.text)
        
		soup = bs(res.text, 'html.parser') 
        
        
		lien = soup.find_all('a')
		lien = [link.get('href') for link in lien]
		filename="nouvel.csv"
		frame = []
		f=open(filename,"w", encoding = 'utf-8')
		entete="Article, url, date, KNPG_M, TM_KNPG, V_M, TM_V, FSD_M, TM_FSD, ASST_M, TM_ASST, JVL_M, TM_JVL\n"
		f.write(entete)
 
		for i in lien:
			res = requests.get(i)
			soup = bs(res.text, 'html.parser') 
			article = soup.find('div', {'class':'detail_content_area'}).find('h2').text
			url = i
			date = soup.find('div', {'class':'detail_content_area'}).find("small").text[10:21].strip()
			KNPG_M = count_words(url, ['Kidnapping', 'Kidnaping', 'Kidnapper'])
			TM_KNPG = bol
			V_M = count_words(url, ['Viol', 'agression', 'sexuelle'])
			TM_V = bol
			FSD_M = count_words(url, ['Fusillade', 'échange de tir', 'coup de feu'])
			TM_FSD = bol
			ASST_M = count_words(url, ['Assassinat', 'homicide', 'crime', 'meurtre'])
			TM_ASST = bol
			JVL_M = count_words(url, ['Jovenel', 'Jovenel Moise', 'Jovenel Moïse', 'Martine Moïse'])
			TM_JVL = bol#converting data to pandas dataframe
			frame.append((article, url,date,KNPG_M,TM_KNPG,V_M,TM_V,FSD_M,TM_FSD,ASST_M,TM_ASST,JVL_M,TM_JVL))
		upperframe.extend(frame)
  
f.close()
data=pd.DataFrame(upperframe, columns=['article', 'url','date','KNPG_M','TM_KNPG','V_M','TM_V','FSD_M','TM_FSD','ASST_M','TM_ASST','JVL_M','TM_JVL'])
data.to_csv('out.csv') # TODO
					
		# init the beautiful instance as html parser
		# soup = bs(res , 'html.parser') # TODO
  
        
	# After collecting the data needed, convert it to pandas dataframe
# TODO

	# then export it as csv
	# df.to_csv('<path/file_name>') # TODO
# else:
# 	print('No working proxy found. Go buy some instead')
