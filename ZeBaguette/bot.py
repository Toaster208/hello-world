import discord

intents = discord.Intents().all()
client = discord.Client(intents)

@client.event
async def on_ready():
    print('Online.')

@client.event
async def on_reaction_add():
    

client.run('MTAwNjYwNDI2NjMzODc4NzM5MQ.GbZOFv.LShB1Ni336rR1DlzsMlTaymFwmloETLF1fl1Bw')