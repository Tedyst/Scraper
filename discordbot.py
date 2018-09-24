import asyncio
from discord import Embed, Server, User
from functii import cauta


async def mesaj(message, client):
    print(message.author.name + ' ' + message.content + ' ' + message.channel.id)
    if str(message.content) == str("/list"):
        await client.send_message(message.channel, 'Ce vrei sa cauti?')
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
        cauta(client)
        await client.send_message(message.channel, "Am facut refresh la preturi!")


# def notify(client, id):
#     user = Server.get_member(str(id))
