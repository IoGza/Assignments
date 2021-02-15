

class RetailItem:

    def __init__(self,item_desc,units_in_inv,price):
        self.__item_desc = item_desc
        self.__units_in_inv = units_in_inv
        self.__price = price
    
    def __str__(self):
        return ("Description: " + str(self.__item_desc) + "\nUnits Available: " + str(self.__units_in_inv) +"\nPrice: " + str(self.__price))
