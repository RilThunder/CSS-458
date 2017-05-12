""""
    Name: Thuan Tran
    CSS 458
    Agent-Based Modeling: Cane Toad
""""
import Desert
import Border
import CTConstant


class SimulationDriver():
    def __init__(self):
        self.phase = 0
        self.size = CTConstant.SIZE
        # Get a 2D List that hold everything: Toad, Border, Desert
        self.theGrid = self.make2dList(self.size, self.size)
        # Keep a list of toad that is available at the moment
        self.listOfToads = []
        self.listOfDesert = []
        self.ToadsLocation = []

    """""
        This method is used to create 2 2D list with a certain size of row and column    
    """""
    # http://www.kosbie.net/cmu/fall-11/15-112/handouts/notes-2d-lists.html
    def make2dList(self, rows, cols):
        a = []
        for row in range(rows): a += [[0] * cols]
        return a

    """""
        This is the method that represent phase 0 of the simulation
      """""
    def phase0(self):
        # Create Desert Agent and place Awps
        # Also placeFencedAwps and init Awp

        for x in range(1, self.size - 1): # Skip the first row
            for y in range(1, self.size - 1):
                self.theGrid[x][y] = Desert()
                self.theGrid[x][y].placeAwps()
                self.theGrid[x][y].placeFencedAwps()
                self.listOfDesert.append(self.theGrid[x][y])
        # After we created Awps, now we need to initialize the surrounding area
        for x in range(1, self.size - 1):
            for y in range(1, self.size - 1):
                if self.theGrid[x][y].isAwp == True:
                    self.theGrid = self.theGrid[x][y].initAwp1(self.theGrid, x, y)
                if self.theGrid[x][y].isAwpFenced == True:
                    self.theGrid = self.theGrid[x][y].initAwp2(self.theGrid, x, y)

        # Create the border around the grid
        for x in range(self.size):
            # Finish Point West
            self.theGrid[x][0] = Border(2, 2)
            # Starting point East
            self.theGrid[x][-1] = Border(-1, -1)
            value = self.theGrid[x][-1].createToads()
            if (value):
                self.listOfToads.append(self.theGrid[x][-1].theToad)
                self.ToadsLocation.append((x, -1))

        # Go through every column in the first and last row and put a Border agent on it
        for x in range(1, self.size):
            # Border on North and South
            self.theGrid[0][x] = Border(-1, -1)
            self.theGrid[-1][x] = Border(-1, -1)
        self.phase = 1

    """""
            This method represent phase 1 of the simulation where they update themselves 
      """""
    def phase1(self):
        for i in self.listOfToads:
            i.toadMayEat()
            i.toadMayDrink()
        for i in self.listOfDesert:
            i.updateFood()
            self.phase = 2

    """""
            This method is used to represent phase 2 of the simulation where the toad now move to a new area 
      """""
    def phase2(self):
        for i in self.listOfToads:
            i.toadMove()
        self.phase = 3
