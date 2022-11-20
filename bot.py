import discord
from discord.ext import commands

client = discord.Client(intents=discord.Intents.default())

TOKEN = 'MTA0MzgyOTI0ODIxMDc4NDI5Ng.Gh9DsP.MvHeKHBf1L0ZqPrasenxr86KaljQpjJjNGnlLU'
#client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello, I am a bot!')
        

""" 
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
 """


client.run(TOKEN)