"""
Author: Evan Putnam
Description: Toolkit to get data from the Runescape grand exchange.
Language: Python3
Pre-Reqs: Beautiful Soup and Requests
"""

from bs4 import BeautifulSoup
import requests


class Item:
    """
    Class that represents a grand exchange item and its stats
    """
    def __init__(self, name, price,today, oneMonth, threeMonth, sixMonth):
        self.name = name
        self.price = price
        self.today = today
        self.oneMonth = oneMonth
        self.threeMonth = threeMonth
        self.sixMonth = sixMonth



class Exchange:
    """
    Class that has varying functions for getting information about runescape items.
    Example of Web Request: http://services.runescape.com/m=itemdb_rs/viewitem?obj=12539
    """
    def __init__(self):
        """
        Base urls for the different items
        """
        self.baseUrl = "http://services.runescape.com/m=itemdb_rs/viewitem?obj="
        self.baseOSRS_URL = "http://services.runescape.com/m=itemdb_oldschool/viewitem?obj="

    def getItemR3(self, id):
        """
        Given an id returns a Item class with information filled
        Runescape 3 Grand Exchange
        :param id: 
        :return Item: 
        """
        req = requests.get(self.baseUrl+str(id))
        data = req.text
        soup = BeautifulSoup(data, "lxml")
        stats = soup.find_all("div", class_="stats")
        for item in stats:
            lst = []
            for prices in item.find_all("span", class_="stats__gp-change"):
                lst.append(prices['title'])
            itemOBJ = Item(soup.title.string, item.find("span")["title"], lst[0], lst[1], lst[2], lst[3])
            return itemOBJ

    def getItemOSRS(self, id):
        """
        Given an id returns a Item class with information filled
        Runescape 3 Grand Exchange
        :param id: 
        :return Item: 
        """
        req = requests.get(self.baseOSRS_URL+str(id))
        data = req.text
        soup = BeautifulSoup(data, "lxml")
        stats = soup.find_all("div", class_="stats")
        for item in stats:
            lst = []
            for prices in item.find_all("span", class_="stats__gp-change"):
                lst.append(prices['title'])
            itemOBJ = Item(soup.title.string, item.find("span")["title"], lst[0], lst[1], lst[2], lst[3])
            return itemOBJ




if __name__ == '__main__':
    ex = Exchange()
    ex.getItemR3(1289000)

    ex.getItemOSRS(7158)
    print(ex.getItemOSRS(7158).name)