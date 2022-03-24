import requests
import random
import pandas as pd
from bs4 import BeautifulSoup as bs

# TODO
proxyUrl = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'

# get the proxy as http response
# TODO
urlReponse = requests.get(proxyUrl)
urlToText = bs(urlReponse.text, 'html.parser')

# Convert the http response to list of proxy
# TODO.
listOfProxy = []
for ip in urlToText.find_all('td', class_='blob-code blob-code-inner js-file-line'):
    ipProxy = ip.text.strip()
    listOfProxy.append(ipProxy)


def get_random_proxy(array):
    # get a random proxy
    proxy = random.choice(array)
    # to get more info on the proxy format
    # More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
    return {'protocol': proxy}  # TODO


def get_working_proxy():
    # test random proxies, to get one that works'''
    TOTAL_TESTS = 20
    for _ in range(TOTAL_TESTS):
        proxy = get_random_proxy(listOfProxy)  # TODO
        try:
            ping = requests.get('https://google.com', proxies=proxy, timeout=3)  # TODO
            # if it works, return it
            if ping.status_code == 200:
                print(f'proxy finded {proxy}')
                return proxy
        except Exception as error:
            print(error)


# set a custom header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    # TODO
}

# call and get the proxy
proxy = get_working_proxy()

targetSite = [
    'https://lenouvelliste.com/national?page=1',
    'https://lenouvelliste.com/national?page=2',
    'https://www.haitilibre.com/flash-infos-1.html',
    'https://www.haitilibre.com/flash-infos-2.html'
]

if proxy:

# hit the target site
# res = requests.get('<target_site>', headers=headers, proxies=proxy) # TODO

# init the beautiful instance as html parser
# soup = bs('<target_content>' , '<parser>') # TODO

# After collecting the data needed, convert it to pandas dataframe
# TODO

# then export it as csv
# 	df.to_csv('<path/file_name>') # TODO
# else:
# 	print('No working proxy found. Go buy some instead')
