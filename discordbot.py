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
    if str(message.content) == str("/list"):
        await client.send_message(message.channel, 'Ce vrei sa cauti?')
        print("Ce vr sa cauti?")
        return

    if message.content.startswith('/list'):
        assignid()
        read = open("emag.txt", "r")
        embed = Embed(
            title="Lista Preturi " + message.content.replace('/list ', ''), description="Pe siteurile Altex si eMAG", color=0x00ff00)

        emag = Pret(0, "")
        lista = []
        initial = []
        for line in read:
            if message.content.replace('/list ', '') in line:
                split1 = line.split('    ')[1].split(
                    ' ', 1)[1].replace('\n', '')
                print(split1 + ' ' + str(id.index(split1)) +
                      ' ')
                if lista[id.index(split1)].val:
                    lista[id.index(split1)] = Pret(
                        int(split1.split(' ')[0]), split1)
                    initial[id.index(split1)] = lista[id.index(split1)]

                if lista[id.index(split1)].val != int(split1.split(' ')[0]):
                    temp = Pret(int(split1.split(' ')[0]), split1)
                    lista[id.index(split1)].next = temp
        for foo in id:
            embed.add_field(
                name=initial[foo].nume, value=initial[foo].traverse(), inline=True)

        await client.send_message(message.channel, embed=embed)
        print(emag.nume + ' ' + emag.next + ' ' + emag.val)

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
        cauta(client)
        await client.send_message(message.channel, "Am facut refresh la preturi!")


# def notify(client, id):
#     user = Server.get_member(str(id))
