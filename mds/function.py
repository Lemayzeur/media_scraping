import requests
from random import choice

PROXY_LIST_URL = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"

def getRandomProxy(proxyList) -> dict:
    return {"http": choice(proxyList)}

def getWorkingProxy()-> dict:
    res = requests.get(PROXY_LIST_URL)
    proxyList = res.text.strip().split('\n')

    print("Getting Working Proxy ...")
    
    for _ in range(20):
        proxy = getRandomProxy(proxyList)
        print("Trying proxy :", proxy['http'], "...")

        try:
            res = requests.get("https://www.google.com/", proxies=proxy, timeout=5)
            if res.status_code == 200:
                print("Proxy", proxy['http'], "found\n")
                return proxy
        except:
            print("Proxy", proxy['http'], "not working, new try ...\n")


def getRequest(url):
    proxy = getWorkingProxy()
    for _ in range(5):
        try:
            print("Request Pending ...")
            res = requests.get(url, proxies=proxy, timeout=10)
            if(res.status_code == 200):
                print("URL :", url,"| Satus Code :", res.status_code, "| Request Success !!!\n")
                return res.text
        except:
            print("Request fail, new try ...")
    print("URL :", url,"Satus Code :", res.status_code, "| Request Failed !!!\n")