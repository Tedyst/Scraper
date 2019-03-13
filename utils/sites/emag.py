import time


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
