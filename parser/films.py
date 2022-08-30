from bs4 import BeautifulSoup
import requests

URL2 = "https://rezka.ag/films/fiction/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []

    for i in items:
        films.append(
            {
                "link": i.find('div', class_="b-content__inline_item-cover").find('a').get('href'),
                "title": i.find('div', class_="b-content__inline_item-link").find('a').getText(),
                "img": i.find('div').find('a').find('img').get('src')
            }
        )
    return films


def parser():
    html = get_html(URL2)
    if html.status_code == 200:
        serials = get_data(html.text)
        return serials
    else:
        raise Exception("Error!")
