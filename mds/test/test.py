from bs4 import BeautifulSoup as Bs
from function import get_request, get_working_proxy

proxy = get_working_proxy()

paj = 1
while paj <= 1:
    content = get_request(f"https://www.haitilibre.com/flash-infos-{paj}.html", proxy=proxy)
    data = Bs(content, "html.parser")
    lista = data.find_all('td', {'class': 'text', 'valign': 'top', 'align': 'left'})

    for td in lista:
        link = td.find('a')['href']

        if "www.icihaiti.com" not in link:
            url = f"https://www.haitilibre.com{link}"
        else:
            url = link

        article = get_request(url, proxy=proxy)

        if article:
            data_art = Bs(article, "html.parser")

            titre = data_art.find('span', {'class': 'titre16color'}).text.strip()
            date = data_art.find('span', {'class': 'date'}).text.strip()

            print(f"{titre}\n{date}\n\n")

    paj += 1

