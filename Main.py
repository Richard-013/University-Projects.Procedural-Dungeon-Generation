import pygame
import Grid

WIN_SIZE = (1000, 1000)

mapSizeX = 100
mapSizeY = 100
maxRoomArea = 1000
minRoomDimension = 15
pathRender = False

print("Please enter the horizontal size of the map: ")
mapSizeX = int(input())
print("Please enter the vertical size of the map: ")
mapSizeY = int(input())
print("Please enter the maximum area one room should occupy: ")
maxRoomArea = int(input())
print("Please enter the minimum dimension a room should have: ")
minRoomDimension = int(input())
print("Do you want auto-generated paths between the rooms: Y/N ")
pathRenderInput = input()

if pathRenderInput == "Y" or pathRenderInput == "y":
    pathRender = True
else:
    pathRender = False

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Grid Test")
mapGrid = Grid.Grid(mapSizeX, mapSizeY, screen, pathRender)
mapGrid.createMap(maxRoomArea, minRoomDimension)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
