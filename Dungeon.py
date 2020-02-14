# Module for dungeon generation
# Richard Horton 2020

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, rooms, xSize, ySize):
        self.numRooms = rooms
        self.mainRegion = Region(0, 0, xSize, ySize) # Root of tree

class Region:
    '''Class for map region - Represents a leaf of the Binary Search Tree'''
    def __init__(self, xHigh, yHigh, xLow, yLow):
        self.xTop = xHigh
        self.yTop = yHigh
        self.xLow = xLow
        self.yLow = yLow

class Room:
    '''Class to store room data'''
    def __init__(self, xHigh, yHigh, xLow, yLow):
        self.xTop = xHigh
        self.yTop = yHigh
        self.xLow = xLow
        self.yLow = yLow

if __name__ == "__main__":
    print("Hello Dungeon")
