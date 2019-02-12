from bs4 import BeautifulSoup
import urllib.request
import time
from logger import log


def findPrice(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('p', attrs={'class': 'product-new-price'}):
            return str(link.contents[0].strip().replace(".", "").replace(" ", "").replace("Lei", "").replace("<sup>", ",").replace("</sup>", "").replace("<span>", "").replace("</span>", "")) + " eMAG "
    if "altex" in url:
        for link in soup.find_all('span', attrs={'class': 'Price-int'}):
            return str(link.contents[0].replace(".", "")) + " Altex "


def fullPage(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('div', attrs={'class': 'card-section-wrapper'}):
            try:
                nume = str(
                    link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt'))
                pret = int(
                    link.contents[5].contents[2].contents[2].contents[0].replace(".", "")) + 1
                timp = int(int(time.time()))
                link = str(link.contents[1].contents[1].contents[0]['href'])
                data = (timp, pret, nume, link, "emag")
                log(data)
            except:
                print("Error : ", link)


def linkType(url):
    if "pd" in url:
        findPrice(url)
    else:
        fullPage(url)
