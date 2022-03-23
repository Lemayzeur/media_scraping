from datetime import datetime
from bs4 import BeautifulSoup as Bs
import pandas as pd
from function import get_request, get_working_proxy

host = "lenouvelliste.com"
pathname = "national"

proxy = get_working_proxy()

articleList = []
pageNumber = 1

while pageNumber:
    content = get_request(f"https://{host}/{pathname}?page={pageNumber}", proxies=proxy)

    endScript = False
    if content:
        data = Bs(content, "html.parser")
        box = data.find_all('div', {'class': 'content_widget'})
        
        for el in box:
            lk = el.find('a')['href']
            print("\t", end='')
            article = get_request(lk, proxies=proxy)
            if article:
                dataArticle = Bs(article, "html.parser")
                boxArt = dataArticle.find("div", {"class": "content_left"})
                
                title = boxArt.find("h2").text.strip()
                contentArt = boxArt.find("article").text.strip()
                date = datetime.strptime(boxArt.find('small').text.strip().split(" ")[2], "%Y-%m-%d")
                print(date.year >= 2019)
                if date.year >= 2019 and date.month >= 3:
                    articleList.append(
                        {
                            "Article": title,
                            "Url": lk,
                            "Date": datetime.strftime(date, "%d-%m-%Y")
                        }
                    )
                else:
                    pageNumber = -1

    pageNumber += 1


print("Create DataFrame ...")
dataframe = pd.DataFrame(articleList)
dataframe.to_csv("nouveliste.csv")
print("Dataframe Save ...")

print("\n\nEND SCRIPT\n\n")
print(f"Page : {pageNumber}\n\n")
