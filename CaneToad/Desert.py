import random
import CTConstant
import Toad


class Desert:
    def __init__(self):

        self.color = None # Color represent the state of the Desert
        self.theToad = None # The living Toad that is on it
        self.isAwpFenced = False # Is this a fenced AWP
        self.isAwp = False
        self.isDesert = True
        self.food = CTConstant.FOOD_CELL
        self.moisture = 0

    def placeAwps(self):
        # Only change if this is not an AWP and there is a chance of changing
        if not self.isAwp:
            if (random.uniform(0, 1.0) < CTConstant.PERCENT_AWP):
                self.isDesert = False
                self.isAwp = True
                self.moisture = 1
                return True
        return False

    def placeFencedAwps(self):
        # Can only change if it is already an AWP and not yet a Fenced pone
        if self.isAwp and self.isAwpFenced == False:
            if (random.uniform(0, 1.0) < CTConstant.PERCENT_AWPS_FENCED):
                self.isAwpFenced = True
                self.moisture = -1
                self.isDesert=False
                self.food = -1
                return True
        return False

    """""
    This method change the corresponding neighbor's moisture to AMT AWP AdJACENT
    """""
    def initAwp1(self, theGrid, x, y):
        # Make sure does not go overboard ( over the border)
        if (x-1 >=0 and y -1 >=0 and x+1 <=CTConstant.SIZE -1 and y+1 <= CTConstant.SIZE-1):
            theGrid[x - 1][y - 1].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x - 1][y].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x - 1][y + 1].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x][y - 1].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x][y + 1].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x + 1][y - 1].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x + 1][y].moisture = CTConstant.AMT_AWP_ADJACENT
            theGrid[x + 1][y + 1].moisture = CTConstant.AMT_AWP_ADJACENT
        return theGrid

    """""
       This method change the corresponding neighbor's neightbor's moisture to AMT AWP OVER2
       """""
    def initAwp2(self, theGrid, x, y):
        # Make sure do not go over the boundary
        if (x -2 >= 0 and y -2 >=0 and y+2 <= CTConstant.SIZE -1 and x+2 <= CTConstant.SIZE-1):
            theGrid[x - 2][y - 2].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x - 2][y - 1].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x - 2][y].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x - 2][y + 1].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x - 2][y + 2].moisture = CTConstant.AMT_AWP_OVER2


            theGrid[x - 1][y - 2].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x - 1][y + 2].moisture = CTConstant.AMT_AWP_OVER2

            theGrid[x][y - 2].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x][y + 2].moisture = CTConstant.AMT_AWP_OVER2

            theGrid[x + 1][y - 2].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x + 1][y + 2].moisture = CTConstant.AMT_AWP_OVER2

            theGrid[x + 2][y - 2].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x + 2][y - 1].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x + 2][y].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x + 2][y + 1].moisture = CTConstant.AMT_AWP_OVER2
            theGrid[x + 2][y + 2].moisture = CTConstant.AMT_AWP_OVER2
        return theGrid

    def updateFood(self):
        # See how much the toad at this position eat
        amountEaten = self.theToad.eat()
        self.food = self.food - amountEaten

    def makeUnfenced(self):
        self.isAwpFenced = False

    def makeFenced(self):
        if (self.isAwp):
            self.isAwpFenced = True
