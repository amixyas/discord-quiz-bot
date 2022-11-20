import discord


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hello, I am a bot!')
        
        
client.run('MTA0MzgyOTI0ODIxMDc4NDI5Ng.GrTuUm.X3rXFXazpiEkT15KfCf17YpNJgC4Mfq1qbABhg')