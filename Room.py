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
        fullRoomChance = randint(0, 100)
        if fullRoomChance <= 5:
            # Room is the entire region
            return True
        else:
            # Generate random area as room
            return False
        # Decide if room will be the entire region or only some of it
        # If only some, generate room co-ordinates for high and low points
        # Set the entry point of the room
        # Set the exit point of the room
        return True

    def generateRoomLow(self):
        return True

    def generateRoomHigh(self):
        return True

    def setEntrance(self):
        # Set the entrance location for the room
        return True

    def setExit(self):
        # Set the exit location for the room
        return True
