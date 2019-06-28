from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.error import *
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

        for td in drops:
            info.drops_list.append(td.get_text())
        print(info.drops_list)
        info.composite_list = [info.drops_list[x:x + 4] for x in range(0, len(info.drops_list), 4)]
        print(info.composite_list)




    except HTTPError as e:
        info.composite_list.clear()
        info.error = e
        print("Error: Could not find an item at the url")
        print("The error exprienced was as follows: " + str(e))
    except URLError as e:
        info.composite_list.clear()
        print("The server could not be found")
    except AttributeError as e:
        pass
    else:
        pass
