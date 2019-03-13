from bs4 import BeautifulSoup
import urllib.request
import time
import utils.config as config
if config.use_elasticsearch is True:
    from utils.databases.elasticsearchdb import log
else:
    from utils.databases.filedb import log


def emagFullPage(soup):
    data = []
    for link in soup.find_all('div', attrs={'class': 'card-section-wrapper'}):
        try:
            nume = str(
                link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt'))
            pret = int(
                link.contents[5].contents[2].contents[2].contents[0].replace(".", "")) + 1
            timp = int(int(time.time()))
            link = str(link.contents[1].contents[1].contents[0]['href'])
            data.append([timp, pret, nume, link, "emag"])
        except:
            print("Error : ", link)
    return data


def getPage(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html5lib")
    if "emag" in url:
        return emagFullPage(soup)


def linkType(url):
    if "pd" in url:
        print("Not supported yet!")
    else:
        data = getPage(url)
        log(data)
