''' Module for generating a dungeon map
    Richard Horton 2020 '''

import string
import Region
from Room import Room

OUTPUT_FILE_NAME = "Keywords.txt"

class Map:
    ''' Class for generating the overall map of the dungeon
        Takes xSize and ySize as positive integers to define size of the map
        Takes maxArea as a positive integer to set the maximum size of any one room'''
    def __init__(self, xSize, ySize, maxArea, minDimension, dungeonType):
        self.xSize = xSize
        self.ySize = ySize
        self.maxRegionArea = maxArea
        self.minDimension = minDimension
        self.dungeonType = dungeonType
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

        for currentRegion in self.regions:
            currentRegion.room.generateKeywords(self.dungeonType)
            self.outputKeywords(currentRegion.room)

    def outputKeywords(self, room):
        ''' Outputs the keywords and descriptions for each room to a file'''
        outputFile = open(OUTPUT_FILE_NAME, 'a')
        outputFile.write("Room: " + room.name)
        outputFile.write("\n")
        outputFile.write("---------------------------------------------------")
        outputFile.write("\n")
        outputFile.write("Floor: " + room.floor)
        outputFile.write("\n")
        outputFile.write("Walls: " + room.wall)
        outputFile.write("\n")
        outputFile.write("Feature: " + room.feature)
        outputFile.write("\n")

        if room.door:
            outputFile.write("Door: Room has a Door")
            outputFile.write("\n")
            outputFile.write("Door Type: " + room.doorType)
            outputFile.write("\n")
            outputFile.write("Door Strength: " + room.doorStrength)
            outputFile.write("\n")
            outputFile.write("Door Lock: " + room.lock)
            outputFile.write("\n")
        else:
            outputFile.write("Door: Room does not have a Door")
            outputFile.write("\n")

        outputFile.write("Inahbited: " + room.inhabited)
        outputFile.write("\n")
        outputFile.write("Occupied: " + room.occupied)
        outputFile.write("\n")

        outputFile.write("Loot: " + room.loot)
        outputFile.write("\n")
        outputFile.write("Loot Quality: " + room.lootQuality)
        outputFile.write("\n")

        outputFile.write("Room Description: " + room.roomDescriptor)
        outputFile.write("\n")
        outputFile.write("Corridor Description: " + room.corridorDescriptor)
        outputFile.write("\n\n")
        outputFile.close()

if __name__ == "__main__":
    theMap = Map(100, 100, 200, 10, "Ruin")
    #0, 10, 0, 5, 33
    print(theMap.start)
    #theMap.createRegions()
    #theMap.getUsableRegions()
    for region in theMap.regions:
        #region.room = Room(region.lowPoint, region.highPoint, 10)
        #print((region.room.low, region.room.high))
        theMap.outputKeywords(region.room)
    #print(len(theMap.regions))
