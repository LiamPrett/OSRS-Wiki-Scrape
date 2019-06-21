from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import *
import re

url = ""

def data_fetch():
    try:
        site = url
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')
        print("-----Item Details-----")
        ItemName = soup.select('h1.firstHeading')[0].text.strip()
        print(ItemName)
        Desc = soup.select('p')[0].text.strip()
        Desc = Desc.split(".")
        print(Desc[0])
        print(Desc[1])

        for sibling in soup.find("table",{"class":"infobox"}).tr.next_siblings:
            full_page_info = sibling.get_text()
            if "Tradeable" in full_page_info:
                print("")
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
                destroy = []
                destroy.append(full_page_info[:7])
                destroy.append(full_page_info[7:])
                destroy[0] += " option"
                print(destroy)
            elif "Examine" in full_page_info:
                examine = []
                examine.append(full_page_info[:7])
                examine.append(full_page_info[7:])
                examine[0] += " text"
                print(examine)
            elif "High alch" in full_page_info:
                print("")
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
                lowalch[0] += " value"
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
                    split = volume[0].split(" ")
                    volume[0] = split[0] + " trade " + split[1]
                    print(volume)


    except HTTPError as e:
        print("Error: Could not find an item at the url")
        print("The error exprienced was as follows: " + str(e))
    except URLError as e:
        print("The server could not be found")
    except AttributeError as e:
        print("Tag was not found")
    else:
        pass








