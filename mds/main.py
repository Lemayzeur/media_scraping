import requests
from function import getWorkingProxy
from bs4 import BeautifulSoup as bs


p = getWorkingProxy()
print(p)

# url = "https://www.gov.uk/search/news-and-communications"

# res = requests.get(url)
# data = bs(res.text, 'html.parser')

# titres = data.find_all("a", class_="gem-c-document-list__item-title")
# descriptions = data.find_all("p", class_="gem-c-document-list__item-description")

# for t in titres:
#     print(t.string)