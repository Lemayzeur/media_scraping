from datetime import datetime
from bs4 import BeautifulSoup as Bs
import pandas as pd
from function import getRequest, getWorkingProxy

host = "lenouvelliste.com"
pathname = "national"

proxy = getWorkingProxy()

articleList = []
pageNumber = 1

while True:
    content = getRequest(f"https://{host}/{pathname}?page={pageNumber}", proxies=proxy)

    endScript = False
    if content:
        data = Bs(content, "html.parser")
        box = data.find_all('div', {'class': 'content_widget'})
        
        for el in box:
            lk = el.find('a')['href']
            article = getRequest(lk, proxies=proxy)
            if article:
                dataArticle = Bs(article, "html.parser")
                boxArt = dataArticle.find("div", {"class": "content_left"})
                
                title = boxArt.find("h2").text.strip()
                contentArt = boxArt.find("article").text.strip()
                date = datetime.strptime(boxArt.find('small').text.strip().split(" ")[2], "%Y-%m-%d")
                
                if date.year >= 2019 and date.month <= 3:
                    articleList.append(
                        {
                            "Article": title,
                            "Url": lk,
                            "Date": datetime.strftime(date, "%d-%m-%Y")
                        }
                    )
                    pass
                else:
                    endScript = True

    if not endScript:
        pageNumber += 1
