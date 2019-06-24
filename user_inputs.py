import datetime
import scrape

def greeting():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("Good Morning")
    elif current_time.hour < 17:
        print("Good Afternoon")
    else:
        print("Good Evening")


def what_item():
    item = input("What would you like to search for?: ")
    print("Searching for " + item)
    item = item.replace(" ", "_")
    scrape.url = "http://oldschool.runescape.wiki/w/" + item.lower()
    if "drop_rate" in scrape.url or "_droprate" in scrape.url or "drop_table" in scrape.url or "_droptable" in scrape.url:
        scrape.url = scrape.url.replace("_droprate", "")
        scrape.url = scrape.url.replace("_drop_rate", "")
        scrape.url = scrape.url.replace("_droptable", "")
        scrape.url = scrape.url.replace("_drop_table", "")
        print(scrape.url)
        scrape.drop_rate_fetch()
    else:
        scrape.generic_data_fetch()
