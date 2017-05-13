"""""
    Name: Thuan Tran
    CSS 458
    Agent-Based Modeling: Cane Toad
"""""
import random
import CTConstant
from Toad import Toad


class Border:
    """""
        This method is the constructor for the Border agent
        Depending on their locations, each border agent will have different food and moisture value
    """""
    def __init__(self,theFood,theValue):
        # The Toad at this place
        self.theToad = None
        self.food = theFood
        self.moisture = theValue
        self.isDesert = False

    """""
        This method create starting Toad on the East Border 
    """""
    def createToads(self):
        if random.uniform(0.0,1.0) <= CTConstant.INIT_PERCENT_TOADS:
            self.theToad = Toad()

            return True
        else:
            return False


