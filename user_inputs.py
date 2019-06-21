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
    item = input("What item would you like to search for?: ")
    print("Searching for " + item)
    item = item.replace(" ", "_")
    scrape.url = "http://oldschool.runescape.wiki/w/" + item
