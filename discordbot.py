import asyncio
from discord import Embed, Server, User
from functii import cauta


class Pret:
    def __init__(self, val, nume):
        self.val = val
        self.nume = nume
        self.next = None

    def traverse(self):
        node = self  # start from the head node
        string = ""
        while node != None:
            string += "->" + str(node.val)  # access the node value
            node = node.next  # move on to the next node
        return string


id = []


def assignid():
    read = open("read.txt", "r")
    for line in read:
        temp = line.replace('\n', '')
        if 'emag' in line:
            id.append('eMAG ' + temp.split('|')[1])
        if 'altex' in line:
            id.append('Altex ' + temp.split('|')[1])


async def mesaj(message, client):
    print(message.author.name + ' ' + message.content + ' ' + message.channel.id)
    if str(message).startswith('list'):
        await client.delete_message(message)
    if str(message).startswith('/add'):
        await client.delete_message(message)
    if str(message.content) == str("/list"):
        mesaj = await client.send_message(message.channel, 'Ce vrei sa cauti?')
        await asyncio.sleep(10)
        await client.delete_message(mesaj)
        print("Ce vr sa cauti?")
        return

    if message.content.startswith('/list'):
        read = open("emag.txt", "r")
        embed = Embed(
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
            mesaj = await client.send_message(message.channel, embed=embed)
            await asyncio.sleep(10)
            await client.delete_message(mesaj)

    elif message.content.startswith('/add'):
        write = open("read.txt", "a+")
        read = open("read.txt", "r")
        for line in read:
            if line.startswith(message.content.replace('/add ', '').split(' ')[0]):
                print("Exista deja : " + line)
                mesaj = await client.send_message(message.channel, line)
                await asyncio.sleep(10)
                await client.delete_message(mesaj)
                return
        if "http://" not in message.content:
            mesaj = await client.send_message(message.channel, 'Invalid url: ' + message.content.replace('/add ', ''))
            await asyncio.sleep(10)
            await client.delete_message(mesaj)
            print('Invalid')
            return
        print("Adaugam " + message.content.replace('/add ', ''))
        write.write(message.content.replace('/add ', '').split(' ', 1)
                    [0] + '|' + message.content.replace('/add ', '').split(' ', 1)[1] + "\n")
        mesaj = await client.send_message(message.channel, 'Adaugat ' + message.content.replace('/add ', ''))
        await asyncio.sleep(10)
        await client.delete_message(mesaj)
        write.flush()

    elif message.content.startswith("/run"):
        cauta(client)
        mesaj = await client.send_message(message.channel, "Am facut refresh la preturi!")
        await asyncio.sleep(10)
        await client.delete_message(mesaj)


# def notify(client, id):
#     user = Server.get_member(str(id))
