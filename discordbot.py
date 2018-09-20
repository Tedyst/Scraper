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
        client.send_message(message.channel, 'ce?')
        print("Ce vr sa cauti?")
        return
    if message.content.startswith('/list'):
        read = open("emag.txt", "r")
        ultim = 0
        for line in read:
            if line.endswith(message.content.replace('/list ', '') + "\n"):
                if ultim != int(line.split('    ')[1].split(' ')[0]):
                    await client.send_message(message.channel, line)
                    ultim = int(line.split('    ')[1].split(' ')[0])
    elif message.content.startswith('/add'):
        write = open("read.txt", "a+")
        read = open("read.txt", "r")
        for line in read:
            if line.startswith(message.content.replace('/add ', '').split(' ')[0]):
                print("Exista deja : " + line)
                await client.send_message(message.channel, 'Exista deja: ' + line)
                return
        print("Adaugam " + message.content.replace('/add ', ''))
        write.write(message.content.replace('/add ', '').split(' ', 1)
                    [0] + '|' + message.content.replace('/add ', '').split(' ', 1)[1] + "\n")
        await client.send_message(message.channel, 'Adaugat ' + message.content.replace('/add ', ''))
        write.flush()


client.run('Mjc2OTY0MDU2Mzk5ODcyMDAy.DoVAEA.eJ4ic5KAtj9D13K-LrMc5UWpqBs')
