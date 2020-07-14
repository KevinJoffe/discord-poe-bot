# BotService.py
import os

import discord
from dotenv import load_dotenv

import CurrencyService

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

channel_id = 732615927266541649

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    exalted_price = CurrencyService.get_exalted_price()
    print(exalted_price)

    channel = client.get_channel(channel_id)
    await channel.send('exalted price is ' + str(exalted_price))


## 573780952237473802
    # Print list of members
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

 # @tasks.loop(seconds=5.0)
 #    async def printer(self):
 #        print(self.index)
 #        self.index += 1

# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!hello'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         await client.send_message(message.channel, msg)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server!'
    )

client.run(TOKEN)