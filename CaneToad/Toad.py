import CTConstant
import random
import Desert


class Toad:
    # How many are surviving at the moment
    numberAlive = 0

    # The grid all of toad
    theCoordinates = None

    def __init__(self):
        global theCoordinates
        global numberAlive
        numberAlive = numberAlive + 1
        # X and Y cordinatates of this toad
        self.currentX = 0
        # Start at the east Border
        self.currentY = CTConstant.SIZE-1



        self.amtEat = 0  # Amount Eaten
        self.energy = CTConstant.AMT_MIN_INIT + random.uniform(CTConstant.INIT_RANGE)
        self.water = CTConstant.AMT_MIN_INIT + random.uniform(CTConstant.INIT_RANGE)

        self.availableFood = -1
        self.availableMoisture = -1
        self.food = -1
        self.moisture = -1

    def setX(self,x):
        self.currentX=x

    def setY(self,y):
        self.currentY=y

    def getX(self):
        return self.currentX

    def getY(self):
        return self.currentY



    def toadMayEat(self):
        if self.energy < CTConstant.WOULD_LIKE_EAT:
            self.eat()
        else:
            self.amtEat = 0

    def eat(self):
        # Get the food at the current positon
        self.availableFood = theCoordinates[self.currentX][self.currentY].food
        self.amtEat = min(CTConstant.AMT_EAT, self.availableFood, 1 - self.energy)
        self.energy = self.energy + self.amtEat
        self.water = min(self.water + CTConstant.FRACTION_WATER * self.amtEat, 1.0)

        return self.amtEat

    def toadMayDrink(self):
        if self.water < CTConstant.WOULD_LIKE_DRINK:
            self.drink()

    def drink(self):
        if self.water + CTConstant.AMT_DRINK <= 1.0:
            self.water = self.water + CTConstant.AMT_DRINK
        else:
            self.water = 1.0

    def toadMove(self):
        if self.water < CTConstant.WOULD_LIKE_DRINK:
            self.thirsty()
        else:
            if self.energy < CTConstant.WOULD_LIKE_EAT:
                self.lookForFood()
            else:
                if random.uniform(0, 1.0) < CTConstant.MAY_HOP:
                    self.hopForFun()
                else:
                    self.stayHere()

    def thirsty(self):
        if theCoordinates[self.currentX][self.currentY].isAwp:
            self.stayHere()
            return
        if theCoordinates[self.currentX][self.currentY].isDesert:
            self.lookForMoisture()
            return
        if  self.currentY == CTConstant.SIZE -1 and theCoordinates[self.currentX][self.currentY-1].theToad == None:
            self.moveW()
            return
        self.stayHere()


    def lookForMoisture(self):
            currentMoisture = []
            # Get the moisture in East, South, West, North
            currentMoisture.append(theCoordinates[self.currentX][self.currentY+1].moisture)

            currentMoisture.append(theCoordinates[self.currentX+1][self.currentY ].moisture)

            currentMoisture.append(theCoordinates[self.currentX][self.currentY-1].moisture)

            currentMoisture.append(theCoordinates[self.currentX-1][self.currentY ].moisture)
            max = currentMoisture.index(max(currentMoisture))

            # Move the toad to the new location
            if max == 0:
                theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentY +=1

                theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()
            if max == 1:
                theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentX += 1


                theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()
            if max == 2:
                theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentY -= 1

                theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()
            else:
                if max == 3:
                    theCoordinates[self.currentX][self.currentY].theToad = None
                    self.currentX -= 1

                    theCoordinates[self.currentX][self.currentY].theToad = self
                    self.here()
                    self.useWaterEnergyHopping()





    def here(self):
        self.availableFood = theCoordinates[self.currentX][self.currentY].food
        self.availableMoisture= theCoordinates[self.currentX][self.currentY].moisture

    def stayHere(self):
        self.here()
        self.useWaterEnergySitting()

    def hopHere(self):
        self.here()
        self.useWaterEnergyHopping()

    def moveW(self):
        theCoordinates[self.currentX][self.currentY].theToad = None
        self.currentY -=1
        self.here()
        self.useWaterEnergyHopping()


    def lookForFood(self):
        if self.currentY == CTConstant.SIZE -1 and theCoordinates[self.currentX][self.currentY-1].isDesert:
            self.moveW()
        else:
            if self.currentY == CTConstant.SIZE -1:
                self.stayHere()
            else:
                self.goToFood()





    def goToFood(self):
        currentFood = []
        # Get the Food in East, South, West, North
        currentFood.append(theCoordinates[self.currentX][self.currentY + 1].moisture)

        currentFood.append(theCoordinates[self.currentX + 1][self.currentY].moisture)

        currentFood.append(theCoordinates[self.currentX][self.currentY - 1].moisture)

        currentFood.append(theCoordinates[self.currentX - 1][self.currentY].moisture)
        max = currentFood.index(max(currentFood))
        if max == 1:
            theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentX += 1

            theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        if max == 2:
            theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentY -= 1

            theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        else:
            if max == 3:
                theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentX -= 1

                theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()
            else:
                if max == 0:
                    theCoordinates[self.currentX][self.currentY].theToad = None
                    self.currentY+=1
                    theCoordinates[self.currentX][self.currentY].theToad = self
                    self.here()
                    self.useWaterEnergyHopping()


    def useWaterEnergySitting(self):

    def useWaterEnergyHopping(self):

    def hopForFun(self):

    def changeCounts(self):
