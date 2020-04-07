''' Module for generating rooms within a given region
    Richard Horton 2020 '''

from random import randint

class Room:
    ''' Class for holding all data on a given room in a map
        Takes co-ordinates of two points as tuples/arrays of positive integers,
            sorted into highest and lowest'''
    def __init__(self, lowPoint, highPoint, minDimension):
        self.minDimension = minDimension-1
        self.regionLow = (lowPoint[0]+1, lowPoint[1]+1)
        self.regionHigh = (highPoint[0]-1, highPoint[1]-1)
        self.low = 0
        self.high = 0

        self.entrance = (0, 0)
        self.exit = (0, 0)

        self.generateRoom()

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
            self.low = self.generateRoomLow()
            self.high = self.generateRoomHigh()
        # Set the entry point of the room
        self.entrance = self.setEntrance()
        # Set the exit point of the room
        self.exit = self.setExit()
        #print(fullRoomChance)

    def checkRegionSize(self):
        ''' Check if the region is big enough to hold a random room'''
        if self.regionLow[0] == 0:
            xSize = self.regionHigh[0] - self.minDimension
        else:
            xSize = self.regionHigh[0] - self.regionLow[0]

        if self.regionLow[1] == 0:
            ySize = self.regionHigh[1] - self.minDimension
        else:
            ySize = self.regionHigh[1] - self.regionLow[1]

        if xSize > 0 and ySize > 0:
            return True

        return False

    def generateRoomLow(self):
        ''' Generates co-ordinates of the lowest corner of the room'''
        if self.regionLow[0] >= self.regionHigh[0]-self.minDimension:
            xLow = self.regionLow[0]
        else:
            xLow = randint(self.regionLow[0], self.regionHigh[0]-self.minDimension)
        
        if self.regionLow[1] >= self.regionHigh[1]-self.minDimension:
            yLow = self.regionLow[1]
        else:
            yLow = randint(self.regionLow[1], self.regionHigh[1]-self.minDimension)

        return (xLow, yLow)

    def generateRoomHigh(self):
        ''' Generates co-ordinates of the highest corner of the room'''
        if self.low[0]+self.minDimension >= self.regionHigh[0]:
            xHigh = self.regionHigh[0]
        else:
            xHigh = randint(self.low[0]+self.minDimension, self.regionHigh[0])
        
        if self.low[1]+self.minDimension >= self.regionHigh[1]:
            yHigh = self.regionHigh[1]
        else:
            yHigh = randint(self.low[1]+self.minDimension, self.regionHigh[1])

        return (xHigh, yHigh)

    def setEntrance(self):
        '''Set the entrance location for the room'''
        # Randomly determine wall that the entrance exists on
        axis = randint(0, 10)

        if(axis > 5):
            # Entrance is on the top wall of the room (x-axis)
            return (randint(self.low[0], self.high[0]), self.high[1])
        else:
            # Entance is on the left wall of the room (y-axis)
            return (self.low[0], randint(self.low[1], self.high[1]))

    def setExit(self):
        '''Set the exit location for the room'''
        # Randomly determine wall that the entrance exists on
        axis = randint(0, 10)

        if(axis > 5):
            # Entrance is on the bottom wall of the room (x-axis)
            return (randint(self.low[0], self.high[0]), self.low[1])
        else:
            # Entance is on the right wall of the room (y-axis)
            return (self.high[0], randint(self.low[1], self.high[1]))


if __name__ == "__main__":
    room = Room((0, 0), (20, 20), 4)
    room.generateRoom()
    print(room.low)
    print(room.high)
    print(room.entrance)
    print(room.exit)
