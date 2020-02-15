# Module for dungeon generation
# Richard Horton 2020

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, rooms, xSize, ySize):
        self.numRooms = rooms
        self.xSize = xSize
        self.ySize = ySize
        # Root of the tree and overall region of the entire map
        self.mainRegion = Region(0, 0, self.xSize, self.ySize, None, None)

    def createRegions(self):
        currentRooms = 1
        while currentRooms < self.numRooms:
            # Generate rooms
            print("IGNORE")

class Region:
    '''Class for map region - Represents a leaf of the Binary Search Tree'''
    def __init__(self, x1, y1, x2, y2, parentRegion, regionCode):
        # Bounding co-ordinates of the region
        if(x1 > x2 or x1 == x2):
            self.xHigh = x1
            self.xLow = x2
        else:
            self.xHigh = x2
            self.xLow = x1

        if(y1 > y2 or y1 == y2):
            self.yHigh = y1
            self.yLow = y2
        else:
            self.yHigh = y2
            self.yLow = y1

        # Room Information
        self.room = None
        # Left Child
        self.subRegion1 = None
        # Right Child
        self.subRegion2 = None
        # Parent
        self.parentRegion = parentRegion
        # Used to determine if it is the left or right child
        self.regionCode = regionCode
        # Region Name
        self.name = self.generateName()

    def generateName(self):
        '''Generates a name for the room'''
        if self.parentRegion is None:
            name = "1"
        else:
            name = self.parentRegion.name + '.' + str(self.regionCode)

        return name

    def splitRegion(self):
        '''Split region at a point on the x-axis or y-axis'''
        if self.xHigh - self.xLow > self.yHigh - self.yLow:
            # Split at a point on the x-axis
            print("IGNORE")
        else:
            # Split at a point on the y-axis
            print("IGNORE")

class Room:
    '''Class to store room data'''
    def __init__(self, length, width):
        self.length = length
        self.width = width

if __name__ == "__main__":
    print("Hello Dungeon")
