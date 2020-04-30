''' Module for generating a dungeon map
    Richard Horton 2020 '''

import Region
from Room import Room

OUTPUT_FILE_NAME = "Keywords.txt"

class Map:
    ''' Class for generating the overall map of the dungeon
        Takes xSize and ySize as positive integers to define size of the map
        Takes maxArea as a positive integer to set the maximum size of any one room'''
    def __init__(self, xSize, ySize, maxArea, minDimension, dungeonType, outputName):
        self.xSize = xSize
        self.ySize = ySize
        self.maxRegionArea = maxArea
        self.minDimension = minDimension+1
        self.dungeonType = dungeonType
        self.start = Region.Region(0, self.xSize-2, 0, self.ySize-2, self.maxRegionArea, self.minDimension)
        self.regions = []
        self.region = None
        self.OUTPUT_FILE_NAME = outputName
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

    def getUsableRegionsDFS(self):
        ''' Traverses the binary tree of the map to find all leaf nodes which
            each represent a usable region'''
        self.region = None
        def _traversal(currentRegion):
            self.region = currentRegion
            if currentRegion not in self.regions and currentRegion.checkLeaf():
                #Adds unvisited nodes to the visited nodes
                self.regions.append(self.region)
                
            #Recursive call for any node not traversed yet
            if currentRegion.subRegionLeft not in self.regions and currentRegion.subRegionLeft is not None:
                _traversal(currentRegion.subRegionLeft)
            if currentRegion.subRegionRight not in self.regions and currentRegion.subRegionRight is not None:
                _traversal(currentRegion.subRegionRight)

        _traversal(self.start)

    def createRooms(self):
        ''' Creates a room in each of the usable regions'''
        k = 0
        for currentRegion in self.regions:
            name = str(k)

            currentRegion.room = Room(currentRegion.lowPoint, currentRegion.highPoint, self.minDimension, name)
            k = k + 1

        #roomsOverSpec = 0
        for currentRegion in self.regions:
            currentRegion.room.generateKeywords(self.dungeonType)
            self.outputKeywords(currentRegion.room)
            #if currentRegion.room.checkRoomSize() > self.maxRegionArea:
                #roomsOverSpec = roomsOverSpec + 1

        #print(str(100 - (roomsOverSpec/len(self.regions))*100) + " %") 
            

    def outputKeywords(self, room):
        ''' Outputs the keywords and descriptions for each room to a file'''
        outputFile = open(self.OUTPUT_FILE_NAME, 'a')
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

        outputFile.write("Inhabited: " + room.inhabited)
        outputFile.write("\n")
        outputFile.write("Occupied: " + room.occupied)
        outputFile.write("\n")

        if room.enemies is not None:
            outputFile.write("Number of Enemies: " + room.enemies)
            outputFile.write("\n")
            outputFile.write("Encounter Difficulty: " + room.enemyDifficulty)
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
