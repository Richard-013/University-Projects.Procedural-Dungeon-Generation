from random import randint

class Room:
    def __init__(self, lowPoint, highPoint):
        self.regionLow = lowPoint
        self.regionHigh = highPoint
        self.low = 0
        self.high = 0

    def generateRoom(self):
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
