import asyncio, discord
from discord.ext import commands
import time

client = commands.Bot(command_prefix='-')
status = False
channel = ''

@client.command()
async def get_channel(ctx):
    global channel
    for channel in client.get_all_channels():
        if 'bump' == channel.name:
            channel = channel.id

@client.event
async def bump():
    print(status, channel)
    while status == True:
        await channel.send("!d bump")
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('bot online')
    await get_channel('x')
    await bump()

@client.event
async def on_guild_join(guild):
    await helpsheet('x')

@client.command()
async def bumpbot(ctx):
    global status
    on_off = True if str(ctx.message.content.split(' ')[1]) == 'on' else False
    msg_color = discord.Color.green() if on_off == True else discord.Color.red()
    status = on_off # change bot on/off status

    embed = discord.Embed(title=("BumpBot is now "+str(status)), color = msg_color)
    await channel.send(embed=embed) # send embedded msg to channel
    await bump()

@client.command()
async def helpsheet(ctx):
    embed = discord.Embed(title="__BumpBot Help Sheet__", description="Please refer to this sheet when using the BumpBot :)", color=discord.Color.purple()) #,color=Hex code
    embed.add_field(name="`-helpsheet`", value="Brings up this sheet!")
    embed.add_field(name="`-bumpbot [on/off]`", value="Turn the bot on or off.")
    await channel.send(embed=embed)

client.run('NzExNDg3MTM1MzQwOTUzNjEw.XsDuBw.-GEUZ8AlxJUkHdYQoErMw4wybIc')


