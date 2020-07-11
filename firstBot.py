import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        
        elif message.content.startswith('bot'):
            await message.channel.send('Whats up {0.author.mention}?'.format(message))

        elif message.content.startswith('When'):
            await message.channel.send('Next tues 03/31 {0.author.mention}'.format(message))

        elif message.content.startswith('form'):
            await message.channel.send("Here it go! Just click on the link https://bit.ly/2y7DlMS {0.author.mention}".format(message))


client = MyClient()
client.run(TOKEN)