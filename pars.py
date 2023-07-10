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






class Parser:
        
    __url = config.url
    __headers = config.headers
    
    def getAllInfo(name: str) -> dict[str, str]:

        index = 1

        req = requests.get(Parser.__url, headers=Parser.__headers)
        soup = BeautifulSoup(req.content, "html.parser")
        crypto_currencies = soup.find("tbody").find_all("tr")

        for tr in crypto_currencies:

            tds = tr.find_all("td")


            if tds[2].text == name:

                index = int(tds[1].find("p").text) - 1

        info = crypto_currencies[index].find_all("td")
        price = info[3].find("span").text
        marketCup = info[7].find_all("span")[1].text
        volume = info[8].find("p").text

        return {
            "price" : price,
            "marketCup" : marketCup,
            "volume" : volume
        }
