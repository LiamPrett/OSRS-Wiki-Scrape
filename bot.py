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

TOKEN = 'NTkyOTg0NTU3MDIwNzc0NDMx.XRHYWA.BdEyZs2PlGqJHsZDCH3ZO6qhRD0'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!price'):
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
        try:
            site = info.url
            hdr = {'User-Agent': 'Mozilla/5.0'}
            req = Request(site, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page, 'html.parser')
            for sibling in soup.find("table", {"class": "infobox"}).tr.next_siblings:
                full_page_info = sibling.get_text()
                if "High alch" in full_page_info:
                    print("")
                    print("-----Item Values-----")
                    info.highalch.append(full_page_info[:9])
                    info.highalch.append(full_page_info[9:])
                    info.highalch[0] += " value"
                    print(info.highalch)

                elif "Low alch" in full_page_info:
                    info.lowalch.append(full_page_info[:8])
                    info.lowalch.append(full_page_info[8:])
                    info.lowalch[0] += " value"
                    print(info.lowalch)
                elif "Store price" in full_page_info:
                    info.storeprice.append(full_page_info[:11])
                    info.storeprice.append(full_page_info[11:])
                    print(info.storeprice)
                elif "Exchange" in full_page_info:
                    if "Grand" in full_page_info:
                        pass
                    else:
                        info.exchange.append(full_page_info[:8])
                        info.exchange.append(full_page_info[8:])
                        info.exchange[1] = info.exchange[1].strip(" (info)")
                        info.exchange[0] += " price"
                        print(info.exchange)
                elif "Buy limit" in full_page_info:
                    info.buylimit.append(full_page_info[:9])
                    info.buylimit.append(full_page_info[9:])
                    print(info.buylimit)
                else:
                    if "Daily volume" in full_page_info:
                        info.volume.append(full_page_info[:12])
                        info.volume.append(full_page_info[12:])
                        split = info.volume[0].split(" ")
                        info.volume[0] = split[0] + " trade " + split[1]
                        print(info.volume)

        except HTTPError as e:
            print("Error: Could not find an item at the url")
            print("The error exprienced was as follows: " + str(e))
        except URLError as e:
            print("The server could not be found")
        except AttributeError as e:
            pass
        else:
            pass
        highalch = info.highalch[1].format(message)
        lowalch = info.lowalch[1].format(message)
        storeprice = info.storeprice[1].format(message)
        exchange = info.exchange[1].format(message)
        buylimit = info.buylimit[1].format(message)
        volume = info.volume[1].format(message)
        await client.send_message(message.channel, "Low Alch Value: " + lowalch + "\n" + "High Alch Value: " + highalch
                                  + "\n" + "Store Price Price: " + storeprice + "\n" + "Grand Exchange Price: " + exchange + "\n"
                                  + "GE Buy Limit: " + buylimit + "\n" + "Daily Trade Volume (Average): " + volume)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
