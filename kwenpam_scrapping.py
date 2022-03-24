import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import random

scheme = 'https'
target_host = 'kwenpam.com'
target_url = f'{scheme}://{target_host}'
print(target_url)
proxy_url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'

#header looks like a browser
header = {
    'Host' : target_host,
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif/image/webp,*/*;q=0.8',
    'Accept-Language' : 'en-US,en;q=0.5',
}

def get_random_proxy(proxy_list):
    #choose a random proxy from the list
    
    proxy = random.choice(proxy_list)
    return{
        'http' : proxy,
    }

def get_working_proxy():
    res = requests.get(proxy_url) #raw text format
    proxy_list = res.text.strip().split('\n')

    total_tries = 20
    print("Getting working proxy...")
    for _ in range(total_tries):
        proxy = get_random_proxy(proxy_list)
        print('%s) Trying proxy %s' % (_ + 1, proxy))
    
        try:
            res = requests.get('https://www.google.com/', proxies=proxy, timeout=3)
            if res.status_code == 200:
                print("One proxy found %s" % proxy)
                return proxy
        except:
            print('Not good\n')
    print(f'We have tried {total_tries} time(s), but no working proxy found')
    
proxy = get_working_proxy()

if proxy:
    #reponse from the target url
    try:
        print('Querying %s...' % target_url)
        response = requests.get(target_url, headers=header, proxies=proxy)
        response.encoding = response.apparent_encoding
        if response.status_code ==200:
            print('Status code: 200')
    
            #Create Beautifulsoup instance
            soup = bs(response.text, 'html.parser')
            
            #dataset
            data = []
            
            divList = soup.find_all('div',{'class' : 'div-item'})
            for div in divList:
                price = div.find('span', {'class' : 'prix-item'}).text
                name = div.find('span', {'class' : 'nom-item'}).text.title()

                name = name.strip().replace('\t','').replace('\r','').replace('\n','')
                price = price.strip().replace('\t','').replace('\r','').replace('\n','')

                data.append(
                    
                    {
                        'name':name,
                        'price' : price,
                    }
                )
            
            #convert datalist to csv file with pandas
            df = pd.DataFrame(data)
            df.to_csv('kwenpam_data.csv')
            
        else:
            print('Request failed with status code', response.status_code)
    except Exception as err:
        print('Request failed', err)
        