import discord
#from discord.ext import commands
import requests
import json
import asyncio

client = discord.Client(intents=discord.Intents.default())

client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:9000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = id
        
        id += 1 
    
    return(qs, answer)


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


""" 
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hello, I am a bot!') 
"""


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$question'):

        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit() 

        try:
            guess = await client.wait_for('message', check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send('Oops. That is not right')

     

""" 
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')
 """



TOKEN = ''
client.run(TOKEN)