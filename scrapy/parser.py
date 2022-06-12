import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST3 = "http://www.ts.kg/category/films"
HOST2 = "https://shisha.kg/catalog/elektronnye_sigarety_vape/odnorazovye_sigarety/"
HOST = "https://doramy.club/genre/kriminal"
HEADER = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


@csrf_exempt
def get_html(URL):
    request = requests.get(url=URL, headers=HEADER)
    return request


@csrf_exempt
def get_data_movies(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="show")
    domen2 = "http://www.ts.kg"
    movies = []
    for i in items:
        movies.append(
            {
                "link": domen2 + i.find("a").get("href"),
                "title": i.find("p", class_="show-title").get_text(),
                "image": domen2 + i.find("a").find("img").get("src"),
            }
        )
    return movies


@csrf_exempt
def get_data_shisha(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="catalog_item main_item_wrapper item_wrap")
    domen = "https://shisha.kg"
    domen2 = "https:"
    vapes = []
    for i in items:
        vapes.append(
            {
                "link": domen + i.find("a").get("href"),
                "title": i.find("div", class_="item-title")
                .find("span")
                .get_text(strip=True),
                "image": domen2 + i.find("a").find("img").get("src"),
            }
        )
    return vapes


@csrf_exempt
def get_data_dorama(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="post-home")
    doramas = []
    for i in items:
        doramas.append(
            {
                "link": i.find("a").get("href"),
                "title": i.find("a").find("span").get_text(),
                "image": i.find("a").find("img").get("src"),
            }
        )
    return doramas


@csrf_exempt
def parser_func_dorama():
    html = get_html(HOST)
    if html.status_code == 200:
        dorama = []
        for i in range(1, 183):
            html = get_html(f"https://doramy.club/strana/yuzhnaya-koreya/page/{i}")
            dorama.extend(get_data_dorama(html.text))
            return dorama
    else:
        raise Exception("Error in parser function dorama")


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        doramas = []
        for i in range(0, 1):
            doramas.extend(get_data_dorama(html.text))
        return doramas
    else:
        raise Exception("Error in parser function")


@csrf_exempt
def parser_func_movies():
    html = get_html(HOST3)
    if html.status_code == 200:
        movies = []
        movies.extend(get_data_movies(html.text))
        return movies
    else:
        raise Exception("Error in parser function, Try again")


@csrf_exempt
def parser_func_vapes():
    html = get_html(HOST2)
    if html.status_code == 200:
        vapes = []
        vapes.extend(get_data_shisha(html.text))
        return vapes
    else:
        raise Exception("Error in parser function, Try again")


#
# c = 0
# while c != 4:
#     html = get_html(HOST)
#     get_data_dorama(html.text)
#     # txt = open('list.txt', 'w')
#     # parse = get_data_dorama(html.text)
#     # conv = '\n'.join(parse)
#     # parsed = txt.write(conv)
#     c += 1
#     continue
