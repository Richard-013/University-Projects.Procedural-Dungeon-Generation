# Module for dungeon generation
# Richard Horton 2020

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, rooms, xSize, ySize):
        self.numRooms = rooms
        # Root of the tree and overall region of the entire map
        self.mainRegion = Region(0, 0, xSize, ySize, None, None)

class Region:
    '''Class for map region - Represents a leaf of the Binary Search Tree'''
    def __init__(self, xHigh, yHigh, xLow, yLow, parentRegion, regionCode):
        # Bounding co-ordinates of the region
        self.xTop = xHigh
        self.yTop = yHigh
        self.xLow = xLow
        self.yLow = yLow
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
            name = 1
        else:
            name = self.parentRegion.name + str(self.regionCode)

        return name

class Room:
    '''Class to store room data'''
    def __init__(self, length, width):
        self.length = length
        self.width = width

if __name__ == "__main__":
    print("Hello Dungeon")
