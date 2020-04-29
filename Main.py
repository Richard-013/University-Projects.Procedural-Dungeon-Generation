''' Main file used to run the procedural generation sytem'''

import random
from datetime import datetime
import pygame
import Grid

WIN_SIZE = (1000, 1000)
OUTPUT_FILE_NAME = "Keywords.txt"


# Set default values
mapSize = 100
maxRoomArea = 500
minRoomDimension = 15
dungeonType = 5
dungeonTypeStr = "Dungeon"
pathRender = True

print("Please enter the size of the map (100 or less recommended): ")
mapSizeX = int(input())
print("Please enter the maximum area one room should occupy: ")
maxRoomArea = int(input())
print("Please enter the minimum dimension a room should have (4 or higher recommended): ")
minRoomDimension = int(input())
print("What type of dungeon would you like?")
print("1 - Tomb\n2 - Ruin\n3 - Dungeon\n4 - Forest\n5 - Random\n")
dungeonType = int(input())
print("Do you want auto-generated paths between the rooms: Y/N ")
pathRenderInput = input()

if dungeonType == 5:
    random.seed(datetime.now())
    dungeonType = random.randint(1, 4)

if dungeonType == 1:
    dungeonTypeStr = "Tomb"
elif dungeonType == 2:
    dungeonTypeStr = "Ruin"
elif dungeonType == 3:
    dungeonTypeStr = "Dungeon"
elif dungeonType == 4:
    dungeonTypeStr = "Forest"

if pathRenderInput == "Y" or pathRenderInput == "y":
    pathRender = True
else:
    pathRender = False


outputFile = open(OUTPUT_FILE_NAME, 'w')
outputFile.write("Dungeon Keywords:\n")
outputFile.write("Dungeon Style: " + dungeonTypeStr + "\n\n")
outputFile.close()

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Grid Test")
mapGrid = Grid.Grid(mapSize, mapSize, screen, pathRender)
mapGrid.createMap(maxRoomArea, minRoomDimension, dungeonTypeStr, OUTPUT_FILE_NAME)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
