import discord
import scrape
import bs4
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import *
import re
import time
import info


def drop_table_fetch():
    try:
        site = info.url
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        print("-----Drop Rate Info-----")
        drops = soup.find("table",{"class":"item-drops"}).findAll("td")
        loop = 1
        for td in drops:
            info.drops_list.append(td.get_text())
            if loop is 1:
                info.drops_table["Name"] = (td.get_text())
                loop += 1
            elif loop is 2:
                info.drops_table["Combat Level"] = (td.get_text())
                loop += 1
            elif loop is 3:
                info.drops_table["Drop Amount"] = (td.get_text())
                loop += 1
            else:
                if loop is 4:
                    info.drops_table["Drop Rate"] = (td.get_text())
                    loop = 1
        print(info.drops_list)
        info.composite_list = [info.drops_list[x:x + 4] for x in range(0, len(info.drops_list), 4)]
        print(info.composite_list)




    except HTTPError as e:
        info.error = e
        print("Error: Could not find an item at the url")
        print("The error exprienced was as follows: " + str(e))
    except URLError as e:
        print("The server could not be found")
    except AttributeError as e:
        pass
    else:
        pass
