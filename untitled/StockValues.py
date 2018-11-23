import Scraper.py
import array

#this class is used to be an instance of a certain foriegn currency
#it stores the values of the currency throughout the day and holds the name
#of said currency
class ForexObject:
    'Common object to represent each stock/forex'
    priceValues = []
    name = ""

    #intialize the Object
    def __init__(self, names):
        self.name = names

    #function to add a value to the array that stores the prices
    def addValue(self, value):
        self.priceValues.append(value)
