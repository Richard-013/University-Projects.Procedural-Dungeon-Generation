''' Module for generating rooms within a given region
    Richard Horton 2020 '''

from random import randint

class Room:
    ''' Class for holding all data on a given room in a map
        Takes co-ordinates of two points as tuples of positive integers,
            sorted into highest and lowest'''
    def __init__(self, lowPoint, highPoint):
        self.minDimension = 3
        self.regionLow = lowPoint
        self.regionHigh = highPoint
        self.low = 0
        self.high = 0

    def generateRoom(self):
        ''' Generates co-ordinates of the room within the bounds of the region'''
        if self.checkRegionSize():
            fullRoomChance = randint(0, 100)
        else:
            # If the region is already 3x3 set the whole region as the room
            fullRoomChance = 100
        if fullRoomChance >= 95:
            # Room is the entire region
            self.low = self.regionLow
            self.high = self.regionHigh
        else:
            # Generate random area as room
            self.low = self.generateRoomLow
            self.high = self.generateRoomHigh
        # Set the entry point of the room
        self.setEntrance()
        # Set the exit point of the room
        self.setExit()

    def checkRegionSize(self):
        ''' Check if the region is big enough to hold a random room'''
        xSize = self.regionLow[0] - self.regionHigh[0]
        ySize = self.regionLow[1] - self.regionHigh[1]
        if xSize > 1:
            return True
        if ySize > 1:
            return True
        return False

    def generateRoomLow(self):
        ''' Generates co-ordinates of the lowest corner of the room'''
        return True

    def generateRoomHigh(self):
        ''' Generates co-ordinates of the highest corner of the room'''
        return True

    def setEntrance(self):
        # Set the entrance location for the room
        return True

    def setExit(self):
        # Set the exit location for the room
        return True
