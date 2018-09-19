from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
import decimal
from datetime import datetime
import time
import schedule

f = open("emag.txt", "a+")
read = open("read.txt", "r")


def findLinks(url, base):
    userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    req = Request(url, None, {'User-Agent': userAgent})
    html = urlopen(req).read()
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
            print data


def findPrice(url):
    userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    req = Request(url, None, {'User-Agent': userAgent})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")
    if "emag" in url:
        for link in soup.find_all('p', attrs={'class': 'product-new-price'}):
            return link.contents[0].strip().replace(".", "").replace(" ", "").replace("Lei", "").replace("<sup>", ",").replace("</sup>", "").replace("<span>", "").replace("</span>", "") + " eMAG "
    if "altex" in url:
        for link in soup.find_all('span', attrs={'class': 'Price-int'}):
            return link.contents[0] + " Altex "


def log(rezultat):
    print rezultat
    f.write("[" + datetime.now().strftime('%c')+"]    " + rezultat + "\n")


def cauta():
    for line in read:
        log(findPrice(line.split("|")[0]) +
            line.split("|")[1].replace('\n', ''))
    f.flush()
    print "Citit perturile la " + datetime.now().strftime('%c')


cauta()

schedule.every(1).hour.do(cauta)

while 1:
    schedule.run_pending()
    time.sleep(1)
