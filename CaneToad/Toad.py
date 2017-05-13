"""""
Name: Thuan Tran
CSS 458
Angent-Base Modeling: Cane Toad
"""""

import CTConstant
import random

"""""
This is a class that is the representation of a toad
This class has multiple methods that allow the toad to do all sort of things
"""""


class Toad:
    """
    Global variables for all toads
    """
    # How many are surviving at the moment
    numberAlive = 0
    numberDead = 0
    numberMigrated  =0

    # The grid all of toad, this will be composed of both Border and Desert class
    theCoordinates = None

    """""
    This is the constructor for the toad
    The constructor will initilize a random energy and water for the toad
    """""

    def __init__(self):

        # Every time the constructor is initialized
        Toad.numberAlive = Toad.numberAlive + 1
        # X and Y cordinatates of this toad
        self.currentX = 0
        # Start at the east Border
        self.currentY = CTConstant.SIZE - 1
        self.state = 1
        self.amtEat = 0  # Amount Eaten

        self.energy = CTConstant.AMT_MIN_INIT + random.uniform(0,CTConstant.INIT_RANGE)
        self.water = CTConstant.AMT_MIN_INIT + random.uniform(0,CTConstant.INIT_RANGE)

        self.availableFood = -1
        self.availableMoisture = -1
        self.food = -1
        self.moisture = -1

    """""
    This is the method that indidicate the toad may eat
    If it is hungry then it eat, else it won't
    """""

    def toadMayEat(self):
        if self.energy < CTConstant.WOULD_LIKE_EAT:
            self.eat()
        else:
            self.amtEat = 0

    """""
        This is the eat method for the toad
        The toad will get the food at the current location on the grid
        """""

    def eat(self):
        # Get the food at the current positon
        self.availableFood = Toad.theCoordinates[self.currentX][self.currentY].food
        self.amtEat = min(CTConstant.AMT_EAT, self.availableFood, 1 - self.energy)
        self.energy = self.energy + self.amtEat
        self.water = min(self.water + CTConstant.FRACTION_WATER * self.amtEat, 1.0)

        return self.amtEat

    """""
        This is the method that indicate ask if a toad want to drink some water
        
    """""

    def toadMayDrink(self):
        if self.water < CTConstant.WOULD_LIKE_DRINK:
            self.drink()

    """""
           This is the drink method of the toad 
           The method will drink a portion of water or reset to 1 if the current water is over 1
    """""

    def drink(self):
        if self.water + CTConstant.AMT_DRINK <= 1.0:
            self.water = self.water + CTConstant.AMT_DRINK
        else:
            self.water = 1.0

    """""
           This is the method that move a toad
           The method will move a toad if it is hungry or thirsty or it might just jump around or stay where it is 
    """""

    def toadMove(self):
        if self.water < CTConstant.WOULD_LIKE_DRINK:
            self.thirsty()
        else:
            if self.energy < CTConstant.WOULD_LIKE_EAT:
                self.lookForFood()
            else:
                # A chance to jump around ?
                if random.uniform(0, 1.0) < CTConstant.MAY_HOP:
                    self.hopForFun()
                else:
                    self.stayHere()

    """""
           This is the method that check if a toad is thirsty
           The method will check for its surrounding area and decided where to go to look for water
       """""
    def thirsty(self):

        if self.currentX == 0 or self.currentX == CTConstant.size -1 or self.currentY == 0 or self.currentY == CTConstant.size -1:
            return
        if Toad.theCoordinates[self.currentX][self.currentY].isAwp:
            self.stayHere()
            return
        if Toad.theCoordinates[self.currentX][self.currentY].isDesert:
            self.lookForMoisture()
            return
        if self.currentY == CTConstant.SIZE - 1 and Toad.theCoordinates[self.currentX][self.currentY - 1].theToad == None:
            self.moveW()
            return
        self.stayHere()

    """""
           This is the method that look for the moisture of of the surrounding Von-Neumann area
            The toad will jump to the one that has the largest moisture 
       """""
    def lookForMoisture(self):
        currentMoisture = []
        # Get the moisture in East, South, West, North
        currentMoisture.append(Toad.theCoordinates[self.currentX][self.currentY + 1].moisture)

        currentMoisture.append(Toad.theCoordinates[self.currentX + 1][self.currentY].moisture)

        currentMoisture.append(Toad.theCoordinates[self.currentX][self.currentY - 1].moisture)

        currentMoisture.append(Toad.theCoordinates[self.currentX - 1][self.currentY].moisture)
        max = currentMoisture.index(max(currentMoisture))

        # Move the toad to the new location
        if max == 0:
            # Set the current location to be Toad Free
            Toad.theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentY += 1
            # Place the toad in the new location
            Toad.theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        if max == 1:
            Toad.theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentX += 1

            Toad.theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        if max == 2:
            Toad.theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentY -= 1

            Toad.theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        else:
            if max == 3:
                Toad.theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentX -= 1

                Toad.theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()

    """""
            This is the method that update the avaialbe food and moisture at current location 

    """""
    def here(self):
        self.availableFood = Toad.theCoordinates[self.currentX][self.currentY].food
        self.availableMoisture = Toad.theCoordinates[self.currentX][self.currentY].moisture

    """""
            This is the method that indicate the toad want to stay here
            The toad will also use water energy while sitting as well 
    """""
    def stayHere(self):
        self.here()
        self.useWaterEnergySitting()

    """""
            This is the method that look for the moisture of of the surrounding Von-Neumann area
            The toad will jump to the one that has the largest moisture 
    """""
    def hopHere(self):
        self.here()
        self.useWaterEnergyHopping()

    """""
            This method is used to move all the toad west
    """""
    def moveW(self):
        Toad.theCoordinates[self.currentX][self.currentY].theToad = None
        self.currentY -= 1
        self.here()
        self.useWaterEnergyHopping()

    """""
            This method is used by the toad to look for nearby Food
    """""
    def lookForFood(self):
        # On a Desert
        if self.currentY == CTConstant.SIZE - 1 and Toad.theCoordinates[self.currentX][self.currentY - 1].isDesert:
            self.moveW()
        else:
            # At the start border
            if self.currentY == CTConstant.SIZE - 1:
                self.stayHere()
            else:
                self.goToFood()

    """""
        This method is used by the toad to go to the nearest food 
        This method also work in the same way as lookForMoisture where it look for the surrounding Von-Newuman neighbors
    """""
    def goToFood(self):
        currentFood = []
        # Get the Food in East, South, West, North
        currentFood.append(Toad.theCoordinates[self.currentX][self.currentY + 1].food)

        currentFood.append(Toad.theCoordinates[self.currentX + 1][self.currentY].food)

        currentFood.append(Toad.theCoordinates[self.currentX][self.currentY - 1].food)

        currentFood.append(Toad.theCoordinates[self.currentX - 1][self.currentY].food)
        max = currentFood.index(max(currentFood))
        if max == 1:
            Toad.theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentX += 1

            Toad.theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        if max == 2:
            Toad.theCoordinates[self.currentX][self.currentY].theToad = None
            self.currentY -= 1

            Toad.theCoordinates[self.currentX][self.currentY].theToad = self
            self.here()
            self.useWaterEnergyHopping()
        else:
            if max == 3:
                Toad.theCoordinates[self.currentX][self.currentY].theToad = None
                self.currentX -= 1

                Toad.theCoordinates[self.currentX][self.currentY].theToad = self
                self.here()
                self.useWaterEnergyHopping()
            else:
                if max == 0:
                    Toad.theCoordinates[self.currentX][self.currentY].theToad = None
                    self.currentY += 1
                    Toad.theCoordinates[self.currentX][self.currentY].theToad = self
                    self.here()
                    self.useWaterEnergyHopping()

    """""
        This method is used by the toad when it does nothing and just sit around
    """""
    def useWaterEnergySitting(self):
        # Check if it is on the start border or on a desert
        if self.currentY == CTConstant.SIZE - 1:
            self.energy = self.energy - 0.5 * CTConstant.ENERGY_HOPPING
            self.water = self.water - 0.5 * CTConstant.WATER_HOPPING
            return
        if self.theCoordinates[self.currentX][self.currentY].isDesert:
            self.energy = self.energy - 0.5 * CTConstant.ENERGY_HOPPING
            self.water = self.water - 0.5 * CTConstant.WATER_HOPPING
            return

        self.energy = self.enery - 0.5 * CTConstant.ENERGY_HOPPING

    """""
        This method is used by the toad when it does nothing and just sit around
    """""
    def useWaterEnergyHopping(self):
        # Check if it on the start border or on the desert
        if self.currentY == CTConstant.SIZE - 1 or self.theCoordinates[self.currentX][self.currentY].isDesert:
            self.energy = self.energy - CTConstant.ENERGY_HOPPING
            self.water = self.water - CTConstant.WATER_HOPPING
            return
        self.energy = self.energy - CTConstant.ENERGY_HOPPING

    """""
        This method is used by the toad to hop around
    """""
    def hopForFun(self):
        # If the toad is on the start border and left  is a desert then move west

        if self.currentY == CTConstant.SIZE - 1 and self.theCoordinates[self.currentX][self.currentY - 1].isDesert:
            self.moveW()
            return
        # Else just stay here
        if self.currentY == CTConstant.SIZE - 1:
            self.stayHere()
            return
        self.stayHere()

    """""
        This method is used to update the total number of toads that tis available at the moment
        Toad will die if the water, energy go below the threshold
    """""
    def changeCounts(self):
        if self.water < CTConstant.DESICCATE or self.energy < CTConstant.STARVE \
                or self.currentY == 0:

            self.theCoordinates[self.currentX][self.currentY].theToad = None
            if self.currentY == 0:
                Toad.numberMigrated +=1
            else:
                Toad.numberDead +=1

            Toad.numberAlive -= 1

            self.state = 0
            return
