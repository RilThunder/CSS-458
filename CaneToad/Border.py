import random
import CTConstant
import Toad
class Border:

    def __init__(self,theFood,theValue):
        self.theToad = None
        self.food = theFood
        self.moisture = theValue

    def createToads(self):
        if random.uniform(0.0,1.0) <= CTConstant:
            self.theToad = Toad()
            return True
        else:
            return False


