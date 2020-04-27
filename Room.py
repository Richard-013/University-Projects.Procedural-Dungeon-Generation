''' Module for generating rooms within a given region
    Richard Horton 2020 '''

from random import randint

class Room:
    ''' Class for holding all data on a given room in a map
        Takes co-ordinates of two points as tuples/arrays of positive integers,
            sorted into highest and lowest'''
    def __init__(self, lowPoint, highPoint, minDimension, name):
        self.minDimension = minDimension-1
        self.regionLow = (lowPoint[0]+1, lowPoint[1]+1)
        self.regionHigh = (highPoint[0]-1, highPoint[1]-1)
        self.low = 0
        self.high = 0

        self.entrance = (0, 0)
        self.exit = (0, 0)

        self.name = name

        # Room Features
        self.floor = None
        self.wall = None
        self.feature = None
        self.door = None
        self.doorType = None
        self.doorStrength = None
        self.lock = None
        self.inhabited = None
        self.occupied = None
        self.loot = None
        self.lootQuality = None
        self.roomDescriptor = None
        self.corridorDescriptor = None
        self.enemies = None
        self.enemyDifficulty = None

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
        # Place the entrance on the left wall
        if self.minDimension == 3:
            # Set the middle cell as the exit when min dimension is 3
            return (self.low[0]+1, self.low[1])

        return (randint(self.low[0]+1, self.high[0]-1), self.low[1])

    def setExit(self):
        '''Set the exit location for the room'''
        # Place the entrance on the right wall
        if self.minDimension == 3:
            # Set the middle cell as the exit when min dimension is 3
            return (self.low[0]+1, self.high[1])
        
        return (randint(self.low[0]+1, self.high[0]-1), self.high[1])

    def generateKeywords(self, dungeonType):
        ''' Generates the keywords for describing the room'''
        self.generateFloor(dungeonType)
        self.generateWall(dungeonType)
        self.generateDoor(dungeonType)
        self.generateOccupation(dungeonType)
        self.generateLoot()
        self.generateDescriptor(dungeonType)
        self.generateCorridor()
        self.generateFeature()

    def generateFloor(self, dungeonType):
        ''' Generate the descriptor for the floor of the room'''
        floors = ["Dirt", "Grassy", "Wooden", "Stone", "Cobbled", "Tiled", "Marble"]
        if dungeonType == "Forest":
            # Don't give forests artificial floors
            self.floor = floors[randint(0, 1)]
        else:
            self.floor = floors[randint(0, len(floors)-1)]

    def generateWall(self, dungeonType):
        ''' Generate the descriptor for the walls of the room'''
        walls = ["Shrubs", "Trees", "Stone", "Pillars", "Wooden", "Stone with Wooden Supports"]
        if dungeonType == "Forest":
            # Don't give forests artificial walls
            self.wall = walls[randint(0, 1)]
        else:
            self.wall = walls[randint(0, len(walls)-1)]

    def generateDoor(self, dungeonType):
        ''' Determine if there is a door in the room and its features'''
        if dungeonType == "Forest":
            # Don't put doors in forest dungeons
            isDoor = 0
        else:
            isDoor = randint(0, 100)

        if isDoor > 65:
            # Generate a door
            self.door = True
            doorTypes = ["Wooden", "Iron", "Steel", "Iron Gate"]
            self.doorType = doorTypes[randint(0, len(doorTypes)-1)]

            doorStrengths = ["Decrepid", "Flimsy", "Normal", "Sturdy", "Elaborate"]
            self.doorStrength = doorStrengths[randint(0, len(doorStrengths)-1)]

            # Determine if the door is locked and how strongly it is locked
            isLocked = randint(0, 100)
            if isLocked < 75:
                self.lock = "Unlocked"
            elif isLocked >= 75 and isLocked < 85:
                self.lock = "Weak Lock"
            elif isLocked >= 85 and isLocked < 95:
                self.lock = "Average Lock"
            elif isLocked >= 95:
                self.lock = "Strong Lock"
        else:
            # No door
            self.door = False

    def generateOccupation(self, dungeonType):
        ''' Determine if a room is currently occupied and whether people have been there before'''
        currentlyOccupied = randint(0, 100)
        if currentlyOccupied >= 60:
            self.occupied = "Occupants are currently present"
            self.generateEnemies()
        elif currentlyOccupied >= 40:
            self.occupied = "Occupants are not in the room, but are nearby"
            self.generateEnemies()
        else:
            self.occupied = "Room has no current occupants"

        inhabited = randint(0, 100)
        if inhabited < 20:
            if dungeonType == "Tomb" or "Ruin":
                self.inhabited = "Signs of occupation from many years in the past"
            else:
                self.inhabited = "No sign of ever being inhabited"
        elif inhabited < 40:
            self.inhabited = "Traces of occupants from some time ago"
        elif inhabited < 50:
            self.inhabited = "Abandoned a little while ago"
        elif inhabited < 60:
            self.inhabited = "Abandoned in a hurry recently"
        elif inhabited < 75:
            self.inhabited = "Lived in until a few days ago"
        else:
            self.inhabited = "The room is currently being lived in"

    def generateLoot(self):
        ''' Generates the loot present in the room'''
        lootTypes = ["Gold", "Items", "Equipment"]
        lootTypeSelect = randint(0, 100)

        if lootTypeSelect < 40:
            self.loot = lootTypes[0]
        elif lootTypeSelect < 75:
            self.loot = lootTypes[1]
        else:
            self.loot = lootTypes[2]

        lootQuality = ["Poor", "Modest", "Good", "Great", "Significant"]
        lootQualitySelect = randint(0, 100)

        if lootQualitySelect < 30:
            self.lootQuality = lootQuality[0]
        elif lootQualitySelect < 50:
            self.lootQuality = lootQuality[1]
        elif lootQualitySelect < 75:
            self.lootQuality = lootQuality[2]
        elif lootQualitySelect < 90:
            self.lootQuality = lootQuality[3]
        else:
            self.lootQuality = lootQuality[4]

    def generateDescriptor(self, dungeonType):
        ''' Generates a descriptor for the state of the room'''
        if dungeonType == "Forest":
            descriptors = ["Leaf covered", "Surprisingly clean", "Branch-strewn"]
            self.roomDescriptor = descriptors[randint(0, len(descriptors)-1)]
        else:
            descriptors = ["Derelict", "Dirty", "Clean", "Scruffy", "Well-Kept", "Untidy"]
            self.roomDescriptor = descriptors[randint(0, len(descriptors)-1)]

    def generateCorridor(self):
        ''' Generates a descriptor for the corridor out of the room'''
        corridors = ["Narrow", "Wide", "Winding", "Widening"]
        self.corridorDescriptor = corridors[randint(0, len(corridors)-1)]

    def generateFeature(self):
        ''' Generates a feature for the players to investigate/interact with'''
        features = ["Sealed chest", "Trapdoor (Shortcut/Quick Exit)", "Trapdoor (Hidden Room)",
                    "Pristine Fountain", "Decrepid Fountain", "Old Dead Body", "Recent Dead Body",
                    "Book", "Spellbook", "Journal", "Quest-Specific Item", "Note (Quest Clue)",
                    "Note (New Quest Hook)"]
        self.feature = features[randint(0, len(features)-1)]

    def generateEnemies(self):
        ''' Generates a suggestion of an enemy encounter'''
        enemyAmount = randint(0, 10)

        self.enemies = str(enemyAmount)

        difficulties = ["Weak", "Easy", "Average", "Difficult", "Hard"]
        difficultySelect = randint(0, 100)

        if difficultySelect < 30:
            self.enemyDifficulty = difficulties[0]
        elif difficultySelect < 55:
            self.enemyDifficulty = difficulties[1]
        elif difficultySelect < 80:
            self.enemyDifficulty = difficulties[2]
        elif difficultySelect < 95:
            self.enemyDifficulty = difficulties[3]
        else:
            self.enemyDifficulty = difficulties[4]

if __name__ == "__main__":
    room = Room((0, 0), (20, 20), 4, "A")
    room.generateRoom()
    print(room.low)
    print(room.high)
    print(room.entrance)
    print(room.exit)
