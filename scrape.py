from bs4 import BeautifulSoup
import urllib.request
import decimal
import discord
import asyncio
from datetime import datetime
import time
import schedule

f = open("emag.txt", "a+")
read = open("read.txt", "r")


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
            return str(link.contents[0]) + " Altex "


def log(rezultat):
    print(rezultat)
    f.write("[" + datetime.now().strftime('%c')+"]    " + rezultat + "\n")


def cauta():
    for line in read:
        text = findPrice(line.split("|")[0])
        log(text + line.split("|")[1].replace('\n', ''))
    f.flush()
    print("Citit perturile la " + datetime.now().strftime('%c'))
    read.seek(0)

# pt development sa nu imi mai iau rate limiting
# cauta()


schedule.every(12).hours.do(cauta)

import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    print(message.author.name + ' ' + message.content)
    if str(message.content) == str("/list"):
        await client.send_message(message.channel, 'Ce vrei sa cauti?')
        print("Ce vr sa cauti?")
        return

    if message.content.startswith('/list'):
        read = open("emag.txt", "r")
        embed = discord.Embed(
            title="Lista Preturi " + message.content.replace('/list ', ''), description="Pe siteurile Altex si eMAG", color=0x00ff00)
        altex = 0
        emag = 0
        for line in read:
            if message.content.replace('/list ', '') in line:
                if line.split('    ')[1].split(' ')[1] == "eMAG":
                    if emag != int(line.split('    ')[1].split(' ')[0]):
                        embed.add_field(
                            name='eMAG', value=line.split('    ')[1].replace('eMAG', ''), inline=True)
                        # await client.send_message(message.channel, line)
                        emag = int(line.split('    ')[1].split(' ')[0])
                else:
                    if altex != int(line.split('    ')[1].split(' ')[0]):
                        embed.add_field(
                            name='Altex', value=line.split('    ')[1].replace('Altex', ''), inline=True)
                        # await client.send_message(message.channel, line)
                        altex = int(line.split('    ')[1].split(' ')[0])
        if embed:
            await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('/add'):
        write = open("read.txt", "a+")
        read = open("read.txt", "r")
        for line in read:
            if line.startswith(message.content.replace('/add ', '').split(' ')[0]):
                print("Exista deja : " + line)
                await client.send_message(message.channel, line)
                return
        print("Adaugam " + message.content.replace('/add ', ''))
        write.write(message.content.replace('/add ', '').split(' ', 1)
                    [0] + '|' + message.content.replace('/add ', '').split(' ', 1)[1] + "\n")
        await client.send_message(message.channel, 'Adaugat ' + message.content.replace('/add ', ''))
        write.flush()

    elif message.content.startswith("/run"):
        cauta()
        await client.send_message(message.channel, "Am facut refresh la preturi!")


client.run('Mjc2OTY0MDU2Mzk5ODcyMDAy.DoVAEA.eJ4ic5KAtj9D13K-LrMc5UWpqBs')


while 1:
    schedule.run_pending()
    time.sleep(1)
