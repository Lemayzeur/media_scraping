import requests
import random

PROXY_LIST_URL = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"

def getRandomProxy(proxyList) -> dict:
    p = random.choice(proxyList)
    return {
        'http': p,
        'https': p
    }

def getWorkingProxy():
    res = requests.get(PROXY_LIST_URL)
    proxyList = res.text.strip().split('\n')

    print("Getting Working Proxy ...")
    
    while True:
        proxy = getRandomProxy(proxyList)
        print("Trying proxy :", proxy['http'], "...")

        try:
            res = requests.get("http://google.com", proxies=proxy, timeout=4)
            if res.status_code == 200:
                print("Proxy", proxy['http'], "found")
                return proxy
        except:
            print("Proxy", proxy['http'], "not working, new try ...")
