from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
import decimal
import time
import mysql.connector
import schedule
mydb = mysql.connector.connect(
  host="mysql",
  user="tedy",
  passwd="cosica",
  database="tedy"
)
mycursor = mydb.cursor()
sql = "INSERT INTO ryzen (timp, nume, pret) VALUES (%s, %s, %s)"

def findLinks(url):
	userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
	req = Request(url, None, {'User-Agent': userAgent})
	html = urlopen(req).read()	
	soup = BeautifulSoup(html, "lxml")
	if "emag" in url:
		for link in soup.find_all('div',attrs={'class' : 'card-section-wrapper'}):
			nume = str(link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt').split("+", 1)[0].replace(u'\xa0', u' ').split(",", 1)[0].split("Procesor AMD ", 1)[1])
			pret = int(link.contents[5].contents[2].contents[2].contents[0].replace(".",""))
			timp = int(int(time.time()))
			data = (timp, nume, pret)
			print data
			mycursor.execute(sql, data)
			# print(link.contents[5].contents[2].contents[2].contents[0].replace(".","") + " " + link.contents[1].contents[1].contents[0].contents[1].contents[0].get('alt').split("+", 1)[0])
	mydb.commit()

def findPrice(url):
	userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
	req = Request(url, None, {'User-Agent': userAgent})
	html = urlopen(req).read()	
	soup = BeautifulSoup(html, "lxml")
	if "emag" in url:
		for link in soup.find_all('p',attrs={'class' : 'product-new-price'}):
			return decimal.Decimal(link.contents[0].strip().replace(".","").replace(" ","").replace("Lei","").replace("<sup>",",").replace("</sup>","").replace("<span>","").replace("</span>",""))
	if "altex" in url:
		for link in soup.find_all('span',attrs={'class' : 'Price-int'}):
			return decimal.Decimal(link.contents[0])

def cauta():
	findLinks("https://www.emag.ro/procesoare/filter/familie-procesor-f2666,amd-ryzen-7-v24725/familie-procesor-f2666,amd-ryzen-5-v24753/familie-procesor-f2666,amd-ryzen-3-v25688/c?ref=lst_leftbar_2666_25688,lst_leftbar_2666_24753,lst_leftbar_2666_24725")
	print time.time()

cauta()

schedule.every(1).hour.do(cauta)

while 1:
    schedule.run_pending()
    time.sleep(1)