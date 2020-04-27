''' Main file used to run the procedural generation sytem'''

from random import randint
import pygame
import Grid

WIN_SIZE = (1000, 1000)
OUTPUT_FILE_NAME = "Keywords.txt"

outputFile = open(OUTPUT_FILE_NAME, 'w')
outputFile.write("Dungeon Keywords:\n")
outputFile.close()

mapSizeX = 100
mapSizeY = 100
maxRoomArea = 300
minRoomDimension = 15
dungeonType = "Dungeon"
pathRender = True

print("Please enter the horizontal size of the map (100 or less recommended): ")
mapSizeX = int(input())
print("Please enter the vertical size of the map (100 or less recommended): ")
mapSizeY = int(input())
print("Please enter the maximum area one room should occupy: ")
maxRoomArea = int(input())
print("Please enter the minimum dimension a room should have (4 or higher recommended): ")
minRoomDimension = int(input())
print("What type of dungeon would you like?\n1 - Tomb\n2 - Ruin\n3 - Dungeon\n4 - Forest\n5 - Random\n")
dungeonType = int(input())
print("Do you want auto-generated paths between the rooms: Y/N ")
pathRenderInput = input()

if dungeonType == 5:
    dungeonType = randint(0, 4)

if dungeonType == 1:
    dungeonType = "Tomb"
elif dungeonType == 2:
    dungeonType = "Ruin"
elif dungeonType == 3:
    dungeonType = "Dungeon"
elif dungeonType == 4:
    dungeonType = "Forest"

if pathRenderInput == "Y" or pathRenderInput == "y":
    pathRender = True
else:
    pathRender = False

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Grid Test")
mapGrid = Grid.Grid(mapSizeX, mapSizeY, screen, pathRender)
mapGrid.createMap(maxRoomArea, minRoomDimension, dungeonType)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
