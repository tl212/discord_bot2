import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send('This is a test')

    if message.content == 'stream join':
        channel = message.author.voice.channel
        await channel.connect()

client.run(TOKEN)

if __name__ == '__main__':
    client = StreamBot()
    client.run(TOKEN)

