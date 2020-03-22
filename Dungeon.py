# Module for dungeon generation
# Richard Horton 2020

import random

class Dungeon:
    '''Class for generating a dungeon - Represents the whole Binary Search Tree'''
    def __init__(self, xSize, ySize, maxRegionArea):
        self.xSize = xSize-1
        self.ySize = ySize-1
        self.maxRegionArea = maxRegionArea
        # Root of the tree and overall region of the entire map
        self.mainRegion = Region(0, 0, self.xSize, self.ySize, self.maxRegionArea, None, None)
        self.finalRegions = []
        self.createRegions()

    def createRegions(self):
        '''Creates the specified number of regions using BFS to traverse the dungeon tree'''
        totalRegions = 1
        currentRegion = None
        # Queue of unvisited (unsplit) regions
        unvisited = [self.mainRegion]
        # List of visited (split) regions
        visited = []
        while unvisited:
            # Generate regions
            currentRegion = unvisited.pop(0)
            if currentRegion not in visited:
                if currentRegion.splittable:
                    splitStatus = currentRegion.splitRegion()
                    if splitStatus == 0:
                        unvisited.append(currentRegion.subRegion1)
                        unvisited.append(currentRegion.subRegion2)
                        totalRegions = totalRegions + 1
                visited.append(currentRegion)
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

    def createRooms(self):
        '''Creates a room in each region'''
        for currentRegion in self.finalRegions:
            if not currentRegion.splittable:
                currentRegion.room = Room(currentRegion.xLow, currentRegion.xHigh, currentRegion.yLow, currentRegion.yHigh)

class Region:
    '''Class for map region - Represents a leaf of the Binary Search Tree'''
    def __init__(self, x1, y1, x2, y2, maxArea, parentRegion, regionCode):
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

        self.maxArea = maxArea

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
        # Can region be split further
        self.splittable = self.checkSplittable()

        self.room = None

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
            # Selects random split point, +1 and -1 prevent out of bounds co-ordinates
            splitPoint = random.randint(self.xLow+1, self.xHigh-1)
            if self.validSplit(splitPoint, True):
                self.subRegion1 = Region(self.xLow, self.yLow, splitPoint, self.yHigh, self.maxArea, self, 1)
                self.subRegion2 = Region(splitPoint+1, self.yLow, self.xHigh, self.yHigh, self.maxArea, self, 2)
                return 0
        else:
            # Selects random split point, +1 and -1 prevent out of bounds co-ordinates
            splitPoint = random.randint(self.yLow+1, self.yHigh-1)
            if self.validSplit(splitPoint, False):
                self.subRegion1 = Region(self.xLow, self.yLow, self.xHigh, splitPoint, self.maxArea, self, 1)
                self.subRegion2 = Region(self.xLow, splitPoint+1, self.xHigh, self.yHigh, self.maxArea, self, 2)
                return 0
        self.splittable = False
        return 1

    def validSplit(self, splitPoint, x):
        '''Checks if a given split will result in an unplayable room'''
        if x:
            xLength1 = (splitPoint - self.xLow) + 1
            yLength1 = (self.yHigh - self.yLow) + 1
            xLength2 = (self.xHigh - splitPoint+1) + 1
            yLength2 = (self.yHigh - self.yLow) + 1
            area1 = xLength1 * yLength1
            area2 = xLength2 * yLength2
            if area1 > self.maxArea/2 and area2 > self.maxArea/2:
                return True
        else:
            xLength1 = (self.xHigh - self.xLow) + 1
            yLength1 = (splitPoint - self.yLow) + 1
            xLength2 = (self.xHigh - self.xLow) + 1
            yLength2 = (self.yHigh - splitPoint+1) + 1
            area1 = xLength1 * yLength1
            area2 = xLength2 * yLength2
            if area1 > self.maxArea/2 and area2 > self.maxArea/2:
                return True
        return False

    def checkSplittable(self):
        '''Checks if a region can be split further'''
        xLength = (self.xHigh - self.xLow) + 1
        yLength = (self.yHigh - self.yLow) + 1
        area = xLength * yLength
        if area > self.maxArea:
            return True
        else:
            return False

class Room:
    '''Class to store room data'''
    def __init__(self, xLow, xHigh, yLow, yHigh):
        self.regionXLow = xLow
        self.regionXHigh = xHigh
        self.regionYLow = yLow
        self.regionYHigh = yHigh
        self.roomXLow = xLow
        self.roomXHigh = xHigh
        self.roomYLow = yLow
        self.roomYHigh = yHigh

        self.entranceX = None
        self.entranceY = None
        self.exitX = None
        self.exitY = None

        self.makeRoom()

    def makeRoom(self):
        '''Creates a room within the bounds set by the region'''
        return True

    def setEntrance(self):
        '''Sets the entrance point for the room'''
        return True

    def setExit(self):
        '''Sets the exit point for the room'''
        return True

if __name__ == "__main__":
    print("Hello Dungeon")
    dungeon1 = Dungeon(100, 100, 25)
    print("Dungeon Stats:")
    print("xSize: " + str(dungeon1.xSize))
    print("ySize: " + str(dungeon1.ySize))
    print("Main Region:", dungeon1.mainRegion)
    print("\n------------------------------\n")
    print("Attempting Region Generation")
    dungeon1.createRegions()
    print("Success")
    print("\n------------------------------\n")
    print(dungeon1.finalRegions)
