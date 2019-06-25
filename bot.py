# Work with Python 3.6
import discord
import scrape
import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import *
import re
import time
import info
import osrs_price


TOKEN = 'NTkyOTg0NTU3MDIwNzc0NDMx.XRHYWA.BdEyZs2PlGqJHsZDCH3ZO6qhRD0'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #OSRS PRICE COMMAND.
    if message.content.startswith('!price'):
        lowalch = ""
        highalch = ""
        storeprice = ""
        buylimit = ""
        volume = ""
        exchange = ""
        info.lowalch = []
        info.highalch = []
        info.storeprice = []
        info.buylimit = []
        info.volume = []
        info.exchange = []
        info.url = ""
        search_term = message.content
        search_term = search_term[7:]
        item = search_term.replace(" ", "_")
        info.url = "http://oldschool.runescape.wiki/w/" + item.lower()
        print(info.url)
        osrs_price.price_fetch()
        if len(info.highalch) > 1:
            highalch = info.highalch[1].format(message)
        else:
            pass
        if len(info.lowalch) > 1:
            lowalch = info.lowalch[1].format(message)
        else:
            pass
        if len(info.storeprice) > 1:
            storeprice = info.storeprice[1].format(message)
        else:
            pass
        if len(info.exchange) > 1:
            exchange = info.exchange[1].format(message)
        else:
            pass
        if len(info.buylimit) > 1:
            buylimit = info.buylimit[1].format(message)
        else:
            pass
        if len(info.volume) > 1:
            volume = info.volume[1].format(message)
        else:
            pass

        await client.send_message(message.channel, "Low Alch Value: " + lowalch + "\n" + "High Alch Value: " + highalch
                                  + "\n" + "Store Price Price: " + storeprice + "\n" + "Grand Exchange Price: " + exchange + "\n"
                                  + "GE Buy Limit: " + buylimit + "\n" + "Daily Trade Volume (Average): " + volume)

    # WHO IS GRAHAM COMMAND COMMAND
    elif message.content.startswith('!whoisgraham') or message.content.startswith("whoissealpup"):
        await client.send_message(message.channel, "I'm glad you asked!" + "\n" + "https://www.youtube.com/watch?v=3A2P-x8GPxg")

    # LIGHT THE BEACONS COMMAND
    elif message.content.startswith("!beacon") or message.content.startswith("!lightthebeacons"):
        await client.send_message(message.channel, "https://gph.is/12wRTQi")

    # HELP COMMAND
    else:
        if message.content.startswith('!help'):
            await client.send_message(message.channel,
                                      "Currently, the following commands are supported:" + "\n" + "\n" + "1. !prices" + "\n"
                                      + "This is performed by typing '!prices item. For example, '!price rune dagger'" + "\n" + "\n"
                                      + "2. !whoisgraham or !whoissealpup" + "\n" + "Why dont you find out who he is? Im not going to tell you."
                                      +"\n" + "\n" + "3. !beacons or !lightthebeacons" + "\n" + "Type: !beacons or !lightthebeacons to signal the Rohirrim for aid.")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
