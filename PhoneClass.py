

class Phone:
    def __init__(self, manufact, model,retailPrce):
        self.__manufact = manufact
        self.__model = model
        self.__retailPrice = retailPrce

    def get_manufact(self,manufact):
        self.__manufact = manufact
        return self.__manufact

    def get_model(self, model):
        self.__model = model
        return self.__model
    
    def get_retail(self, retailPrice):
        self.__retailPrice = retailPrice
        return self.__retailPrice

    def __str__(self):
        return ("Manufacturer: " + str(self.__manufact) + "\n" + 
                                "Model: " + str(self.__model) + "\n" + 
                                "Retail Price: " + str(self.__retailPrice))