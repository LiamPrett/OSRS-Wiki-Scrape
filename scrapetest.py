from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import *
import re

try:
    site = "http://oldschool.runescape.wiki/w/Rune_scimitar"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site, headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    for sibling in soup.find("table",{"class":"infobox"}).tr.next_siblings:
        full_page_info = sibling.get_text()
        if "Tradeable" in full_page_info:
            print("-----Item Properties-----")
            tradeable = re.findall('[A-Z][a-z]*', full_page_info)
            print(tradeable)
        elif "Equipable" in full_page_info:
            equipable = re.findall('[A-Z][a-z]*', full_page_info)
            print(equipable)
        elif "Stackable" in full_page_info:
            stackable = re.findall('[A-Z][a-z]*', full_page_info)
            print(stackable)
        elif "Noteable"  in full_page_info:
            noteable = re.findall('[A-Z][a-z]*', full_page_info)
            print(noteable)
        elif "Destroy" in full_page_info:
            destroy = re.findall('[A-Z][a-z]*', full_page_info)
            destroy[0] += " option"
            print(destroy)
        elif "Examine" in full_page_info:
            examine = []
            examine.append(full_page_info[:7])
            examine.append(full_page_info[7:])
            examine[0] += " text"
            print(examine)
        elif "High alch" in full_page_info:
            print("\n")
            print("-----Item Values-----")
            highalch = []
            highalch.append(full_page_info[:9])
            highalch.append(full_page_info[9:])
            highalch[0] += " value"
            print(highalch)
        elif "Low alch" in full_page_info:
            lowalch = []
            lowalch.append(full_page_info[:8])
            lowalch.append(full_page_info[8:])
            lowalch[0] += "value"
            print(lowalch)
        elif "Store price" in full_page_info:
            storeprice = []
            storeprice.append(full_page_info[:11])
            storeprice.append(full_page_info[11:])
            print(storeprice)
        elif "Weight" in full_page_info:
            weight = []
            weight.append(full_page_info[:6])
            weight.append(str(full_page_info[6:]))
            weight[1] = weight[1].replace(u'\xa0', u'')
            print(weight)
        elif "Exchange" in full_page_info:
            if "Grand" in full_page_info:
                pass
            else:
                exchange = []
                exchange.append(full_page_info[:8])
                exchange.append(full_page_info[8:])
                exchange[1] = exchange[1].strip(" (info)")
                exchange[0] += " price"
                print(exchange)
        elif "Buy limit" in full_page_info:
            buylimit = []
            buylimit.append(full_page_info[:9])
            buylimit.append(full_page_info[9:])
            print(buylimit)
        else:
            if "Daily volume" in full_page_info:
                volume = []
                volume.append(full_page_info[:12])
                volume.append(full_page_info[12:])
                print(volume)










    # html = urlopen("http://oldschool.runescape.wiki/w/Rune_dagger")
    # bs = BeautifulSoup(html.read(), 'html.parser')
    # nameList = bs.find_all("tr", {"class": "undefined"})
    # for name in nameList:
    #     print(name.get_text())

except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found")
except AttributeError as e:
    print("Tag was not found")
else:
    pass








