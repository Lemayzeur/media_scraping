import requests
from random import choice

PROXY_LIST_URL = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"

def getRandomProxy(proxyList:list) -> dict:
    return {"http": choice(proxyList)}

def getWorkingProxy()-> dict:
    res = requests.get(PROXY_LIST_URL)
    proxyList = res.text.strip().split('\n')

    print("Getting Working Proxy ...")
    
    while True:
        proxy = getRandomProxy(proxyList)
        print("Trying proxy :", proxy['http'], "...")

        try:
            res = requests.get("https://www.google.com/", proxies=proxy, timeout=5)
            if res.status_code == 200:
                print("Proxy", proxy['http'], "found\n")
                return proxy
        except:
            print("Proxy", proxy['http'], "not working, new try ...\n")


def getRequest(url:str, proxies:dict) -> str:
    for _ in range(5):
        try:
            print("Request Pending ...")
            res = requests.get(url, proxies=proxies, timeout=10)
            if(res.status_code == 200):
                print("URL :", url,"| Satus Code :", res.status_code, "| Request Success !!!\n")
                return res.text
            else:
                print("URL :", url,"Satus Code :", res.status_code, "| Request Failed !!!\n")
        except Exception as err:
            print("Connection ERROR -", err)
            print("Request fail, new try ... -")