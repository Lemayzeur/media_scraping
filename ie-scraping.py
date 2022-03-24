import requests
import random
import time
from bs4 import BeautifulSoup as bs

proxyUrl = 'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt'  # TODO

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
    ''' get a random proxy '''
    proxy = random.choice(array)
    # to get more info on the proxy format
    # More info, visit: https://docs.python-requests.org/en/latest/api/#module-requests
    return {'protocol': proxy}  # TODO


def get_working_proxy():
    ''' test random proxies, to get one that works'''
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

targetList = [
    'https://lenouvelliste.com/national?page=2',
    'https://www.haitilibre.com/flash-infos-1.html',
    'https://www.haitilibre.com/flash-infos-2.html'
]

keywordList = [
    'kidnapping', 'viol', 'agression sexuelle', 'fusillade', 'enlevement', 'insécurité',
    'séquestration', 'échange de tir', 'coup de feu', 'affrontement', 'assassinat', 'hommes armés'
                                                                                    'homicide', 'crime', 'meurtre',
    'Jovenel', 'Jovenel Moïse', 'Martine Moïse',
    'suicide'
]

pages = 10
dataset = []
if proxy:
    # hit the target site
    for page in range(0, pages):
        pageRequest = requests.get(f'https://lenouvelliste.com/national?page={page + 1}', headers=headers,
                                   proxies=proxy)  # TODO
        # init the beautiful instance as html parser
        pageContent = bs(pageRequest.text, 'html.parser')  # TODO
        # fnd the class that contain the link i searching
        for content in pageContent.find_all('div', class_='content_widget'):
            # finding the link
            for titleText in content.find_all('a', href=True):
                for link in range(0, len(keywordList)):
                    if keywordList[link] in titleText["href"]:
                        keywordLink = requests.get(titleText["href"])
                        keywordResponse = bs(keywordLink, 'html.parser')
                        print(f' href content: {titleText["href"]}')

            articleTitle = titleText.contents[0]
            for keyword in range(0, len(keywordList)):
                if keywordList[keyword] in articleTitle:
                    print(f'{articleTitle}')
        time.sleep(5)
    # After collecting the data needed, convert it to pandas dataframe
    # TODO

    # then export it as csv
    # df.to_csv('<path/file_name>') # TODO

# else:
# 	print('No working proxy found. Go buy some instead'