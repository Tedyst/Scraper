import asyncio
import discord
from discordbot import mesaj

client = discord.Client()


@client.event
async def on_message(message):
    await client.send_message(id=discord.Client.get_channel(message.channel), "Test")
    await mesaj(message, client)


async def runsearch():
    from functii import cauta
    while True:
        await asyncio.sleep(86400)
        cauta(client)

client.loop.create_task(runsearch())

client.run('Mjc2OTY0MDU2Mzk5ODcyMDAy.DoVAEA.eJ4ic5KAtj9D13K-LrMc5UWpqBs')
