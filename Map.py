''' Module for generating a dungeon map
    Richard Horton 2020 '''

import Region
from Room import Room
import string

class Map:
    ''' Class for generating the overall map of the dungeon
        Takes xSize and ySize as positive integers to define size of the map
        Takes maxArea as a positive integer to set the maximum size of any one room'''
    def __init__(self, xSize, ySize, maxArea, minDimension):
        self.xSize = xSize
        self.ySize = ySize
        self.maxRegionArea = maxArea
        self.minDimension = minDimension
        self.start = Region.Region(0, self.xSize-1, 0, self.ySize-1, self.maxRegionArea, self.minDimension)
        self.regions = []
        self.getUsableRegions()
        self.createRooms()

    def getUsableRegions(self):
        ''' Traverses the binary tree of the map to find all leaf nodes which
            each represent a usable region'''
        def _findUsableRegions(currentRegion):
            if currentRegion is not None:
                if currentRegion.checkLeaf():
                    self.regions.append(currentRegion)
                _findUsableRegions(currentRegion.subRegionLeft)
                _findUsableRegions(currentRegion.subRegionRight)
        _findUsableRegions(self.start)

    def createRooms(self):
        ''' Creates a room in each of the usable regions'''
        k = 0
        for currentRegion in self.regions:
            if k // 26 == 1:
                name = string.digits[k-26]
            else:
                name = string.ascii_uppercase[k]

            currentRegion.room = Room(currentRegion.lowPoint, currentRegion.highPoint, 15, name)
            k = k + 1

if __name__ == "__main__":
    theMap = Map(100, 100, 200, 10)
    #0, 10, 0, 5, 33
    print(theMap.start)
    #theMap.createRegions()
    #theMap.getUsableRegions()
    for region in theMap.regions:
        #region.room = Room(region.lowPoint, region.highPoint, 10)
        print((region.room.low, region.room.high))
    #print(len(theMap.regions))
