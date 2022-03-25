from datetime import datetime
from bs4 import BeautifulSoup as Bs
from function import get_request, get_working_proxy

proxy = get_working_proxy()


def ln_parser(url) -> tuple:
    article_list = []
    year = 2022
    content = get_request(url, proxy=proxy)
    if content:
        data = Bs(content, "html.parser")
        box = data.find_all('div', {'class': 'content_widget'})

        for el in box:
            link = el.find('a')['href']

            print("\t", end='')
            article = get_request(link, proxy=proxy)
            if article:
                data_article = Bs(article, "html.parser")
                box_art = data_article.find("div", {"class": "content_left"})

                title = box_art.find("h2").text.strip().replace(' ', '')
                # content_art = box_art.find("article").text.strip()
                date = datetime.strptime(box_art.find('small').text.strip().split(" ")[2], "%Y-%m-%d")

                article_list.append({'Url': link, 'Article': title, 'Date': datetime.strftime(date, "%d-%m-%Y")})
                year = date.year

    return article_list, year


def hl_parser(url) -> tuple:
    article_list = []
    year = 2022
    content = get_request(url, proxy=proxy)
    if content:
        data = Bs(content, "html.parser")
        box = data.find_all('td', {'class': 'text', 'valign': 'top', 'align': 'left'})

        for el in box:
            link = el.find('a')['href']
            if "www.icihaiti.com" not in link:
                link = f"https://www.haitilibre.com{link}"

            print("\t", end='')
            article = get_request(link, proxy=proxy)
            if article:
                data_art = Bs(article, "html.parser")

                title = data_art.find('span', {'class': 'titre16color'}).text.strip()
                date = datetime.strptime(data_art.find('span', {'class': 'date'}).text.strip(), "%d/%m/%Y %H:%M:%S")

                article_list.append({'Url': link, 'Article': title, 'Date': datetime.strftime(date, "%d-%m-%Y")})
                year = date.year

    return article_list, year
