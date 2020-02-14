# Module for dungeon generation
# Richard Horton 2020

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, rooms, xSize, ySize):
        self.numRooms = rooms
        # Root of the tree
        self.mainRegion = Region(0, 0, xSize, ySize, None)

class Region:
    '''Class for map region - Represents a leaf of the Binary Search Tree'''
    def __init__(self, xHigh, yHigh, xLow, yLow, parentRegion):
        self.xTop = xHigh
        self.yTop = yHigh
        self.xLow = xLow
        self.yLow = yLow
        self.roomLength = None
        self.roomWidth = None
        # Left child
        self.subRegion1 = None
        # Right child
        self.subRegion2 = None
        # Parent
        self.parentRegion = parentRegion

class Room:
    '''Class to store room data'''
    def __init__(self, length, width):
        self.length = length
        self.width = width

if __name__ == "__main__":
    print("Hello Dungeon")
