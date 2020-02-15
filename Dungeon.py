# Module for dungeon generation
# Richard Horton 2020

import random

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, rooms, xSize, ySize):
        self.numRooms = rooms
        self.xSize = xSize
        self.ySize = ySize
        # Root of the tree and overall region of the entire map
        self.mainRegion = Region(0, 0, self.xSize, self.ySize, None, None)
        self.finalRegions = []

    def createRegions(self):
        '''Creates the specified number of regions using BFS to traverse the dungeon tree'''
        totalRegions = 1
        currentRegion = None
        # Queue of unvisited (unsplit) regions
        unvisited = [self.mainRegion]
        # List of visited (split) regions
        visited = []
        while totalRegions < self.numRooms:
            # Generate regions
            currentRegion = unvisited.pop(0)
            if currentRegion not in visited:
                currentRegion.splitRegion()
                unvisited.append(currentRegion.subRegion1)
                unvisited.append(currentRegion.subRegion2)
                visited.append(currentRegion)
                totalRegions = totalRegions + 1
            else:
                continue

        # Gather all regions with no children/sub-regions
        self.collectRegions()

    def collectRegions(self):
        '''Builds a list of regions that have been fully divided using BFS'''
        currentRegion = None
        unvisited = [self.mainRegion]
        visited = []
        while unvisited:
            currentRegion = unvisited.pop(0)
            if currentRegion not in visited:
                if currentRegion.subRegion1 is not None:
                    unvisited.append(currentRegion.subRegion1)
                if currentRegion.subRegion2 is not None:
                    unvisited.append(currentRegion.subRegion2)
                if currentRegion.subRegion1 is None and currentRegion.subRegion2 is None:
                    self.finalRegions.append(currentRegion)
                visited.append(currentRegion)

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
            lowMargin = int(self.xLow+(self.xLow*0.25))
            highMargin = int(self.xHigh-(self.xHigh*0.25))
            splitPoint = random.randint(lowMargin, highMargin)
            self.subRegion1 = Region(self.xLow, self.yLow, splitPoint, self.yHigh, self, 1)
            self.subRegion2 = Region(splitPoint+1, self.yLow, self.xHigh, self.yHigh, self, 2)
        else:
            # Split at a point on the y-axis
            lowMargin = int(self.yLow+(self.yLow*0.25))
            highMargin = int(self.yHigh-(self.yHigh*0.25))
            splitPoint = random.randint(lowMargin, highMargin)
            self.subRegion1 = Region(self.xLow, self.yLow, self.xHigh, splitPoint, self, 1)
            self.subRegion2 = Region(self.xLow, splitPoint+1, self.xHigh, self.yHigh, self, 2)

class Room:
    '''Class to store room data'''
    def __init__(self, length, width):
        self.length = length
        self.width = width

if __name__ == "__main__":
    print("Hello Dungeon")
