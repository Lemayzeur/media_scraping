from urllib.request import Request
import requests
from function import getRequest
from bs4 import BeautifulSoup as bs

url = "https://code9haiti.com/fr/courses/"

data = bs(getRequest(url), "html.parser")

titres = data.find_all("h6", class_="card-title bg-light border-bottom border-top p-1 bold")
desc = data.find_all("p", class_="card-text desc f-12 gray")

for t, d in zip(titres, desc):
    print("Titre :", t.text)
    print("Description :", d.text)