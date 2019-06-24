# OSRS Wiki Scrape

## About the project
This project is a spiritual successor of my selenium based scraping tool of the Grand Exchange. Whilst the selenium project wasn't finished, I found that this project using BeautifulSoup held more possibilities and the opportunity to use a new package.

This project essentially scrapes the OSRS wiki and presents information based on commands entered by the user in the command line. 

## Languages, imports and packages
- Python
- Beautiful Soup (bs4)
- urllib.request
- re
- time

##What can it do?
So far the application can do the following;
- Search for anything on the wiki and return information about said item. This is done by entering a command like "bandos boots", when prompted.
- Search for what NPC's drop an item. This is done by entering a command like "bandos boots drop table", when prompted.
- Search for how much an item is worth. This is done by entering a command like "bandos boots price", when prompted.

## Futute updates
- [ ] More commands, such as: Description, Item Properties etc
- [ ] Search for more than one item in succession
- [ ] Integrate with discord with command support (distant future) 