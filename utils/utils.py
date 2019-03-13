from bs4 import BeautifulSoup
import urllib.request
import utils.config as config
from utils.sites.emag import emagFullPage

if config.use_elasticsearch is True:
    from utils.databases.elasticsearchdb import log
else:
    from utils.databases.filedb import log


def getBigPage(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html5lib")
    if "emag" in url:
        return emagFullPage(soup)


def linkType(url):
    if "pd" in url:
        print("Not supported yet!")
    else:
        data = getBigPage(url)
        log(data)
