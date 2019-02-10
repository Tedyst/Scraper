from bs4 import BeautifulSoup
import urllib.request
import asyncio
from datetime import datetime
import time
# from discordbot import notify

# f = open("emag.txt", "a+")
# read = open("read.txt", "r")


def findLinks(url, base):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('div', attrs={'class': 'card-section-wrapper'}):
            if base == "ryzen":
                nume = str(link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt').split(
                    "+", 1)[0].replace(u'\xa0', u' ').split(",", 1)[0].split("Procesor AMD ", 1)[1])
            if base == "memorie":
                nume = str(link.contents[1].contents[1].contents[0].contents[1].contents[0].get(
                    'alt').split("+", 1)[0].replace(u'\xa0', u' ').split("Memorie ", 1)[1])
            pret = int(
                link.contents[5].contents[2].contents[2].contents[0].replace(".", ""))
            timp = int(int(time.time()))
            data = (timp, nume, pret)
            print(data)


def findPrice(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('p', attrs={'class': 'product-new-price'}):
            return str(link.contents[0].strip().replace(".", "").replace(" ", "").replace("Lei", "").replace("<sup>", ",").replace("</sup>", "").replace("<span>", "").replace("</span>", "")) + " eMAG "
    if "altex" in url:
        for link in soup.find_all('span', attrs={'class': 'Price-int'}):
            return str(link.contents[0].replace(".", "")) + " Altex "


def log(rezultat):
    print(rezultat)
    f.write("[" + datetime.now().strftime('%c')+"]    " + rezultat + "\n")


def cauta(client):
    for line in read:
        text = findPrice(line.split("|")[0])
        log(text + line.split("|")[1].replace('\n', ''))
        # notify(client, line.split("|")[3])
    f.flush()
    print("Citit perturile la " + datetime.now().strftime('%c'))

    read.seek(0)


def fullPage(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('div', attrs={'class': 'card-section-wrapper'}):
            nume = str(
                link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt'))
            pret = int(
                link.contents[5].contents[2].contents[2].contents[0].replace(".", "")) + 1
            timp = int(int(time.time()))
            print(timp, nume, pret)


fullPage("https://www.emag.ro/procesoare/c")
