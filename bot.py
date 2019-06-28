# Work with Python 3.6
import discord
import info
import osrs_price
import drop_table


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

    #DROP TABLE COMMAND
    elif message.content.startswith('!dt'):
        search_term = message.content
        search_term = search_term[4:]
        item = search_term.replace(" ", "_")
        info.url = "http://oldschool.runescape.wiki/w/" + item.lower()
        print(info.url)
        drop_table.drop_table_fetch()
        item_list = ""
        for item in info.composite_list:
            item_list += str(item).strip("[" + "]") + "\n"
        if len(item_list) > 2000:
            middle = ( len(item_list) / 2)
            firstpart = item_list[:int(middle)]
            secondpart = item_list[int(middle):]
            await client.send_message(message.channel, "NPC Name, NPC Level, Drop Amount, Drop Rate")
            await client.send_message(message.channel, firstpart)
            await client.send_message(message.channel, secondpart)
        elif item_list is None or item_list is "":
            await client.send_message(message.channel, "No Results Found - The item either does not have a drop table or your spelling is incorrect")
        else:
            await client.send_message(message.channel, "NPC Name, NPC Level, Drop Amount, Drop Rate")
            await client.send_message(message.channel, item_list)
        info.composite_list.clear()


    # WHO IS GRAHAM COMMAND COMMAND
    elif message.content.startswith('!whoisgraham') or message.content.startswith("whoissealpup"):
        await client.send_message(message.channel, "I'm glad you asked!" + "\n" + "https://www.youtube.com/watch?v=3A2P-x8GPxg")

    # LIGHT THE BEACONS COMMAND
    elif message.content.startswith("!beacon") or message.content.startswith("!lightthebeacons"):
        await client.send_message(message.channel, "https://gph.is/12wRTQi")

    elif message.content.startswith("!github"):
        await client.send_message(message.channel, "https://github.com/LiamPrett/OSRS-Wiki-Scrape")

    # HELP COMMAND
    else:
        if message.content.startswith('!help'):
            await client.send_message(message.channel,
          "Currently, the following commands are supported:" + "\n" + "\n"
            + "1. **!prices**" + "\n" + "This is performed by typing **'!prices item'**. For example, **'!price rune dagger'**" + "\n" + "\n"
            + "2. **!drop table**" + "\n" + "This is performed by typing '**!drop table item**'. For example, '**!drop table bandos boots'**." + "\n" + "\n"
            + "3. **!whoisgraham** or **!whoissealpup**" + "\n" + "Why dont you find out who he is? Im not going to tell you."+ "\n" + "\n"
            + "4. **!beacons** or **!lightthebeacons**" + "\n" + "Type: **!beacons** or **!lightthebeacons** to signal the Rohirrim for aid.")

            await client.send_message(message.channel,
              "*Help commands continued...1*" + "\n" +
              "5. **!github**" + "\n" + "Type: **!github** to get the source code for this bot, as well as updates on upcoming features.")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
