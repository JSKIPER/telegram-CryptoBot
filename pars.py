import config
import requests
from bs4 import BeautifulSoup


def parser(index, url = config.url, headers = config.headers):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    crypto_currencies = soup.find_all("tr")
    info = crypto_currencies[index].find_all("td")
    price = info[3].find("span")
    market_cup = info[7].find_all("span")
    value = info[8].find("p")
    return price, market_cup[1], value






