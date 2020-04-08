import pygame
import Grid

WIN_SIZE = (1000, 1000)

mapSizeX = 100
mapSizeY = 100
maxRoomArea = 1000
minRoomDimension = 15

pygame.init()
screen = pygame.display.set_mode(WIN_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Grid Test")
mapGrid = Grid.Grid(mapSizeX, mapSizeY, screen, True)
mapGrid.createMap(maxRoomArea, minRoomDimension)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
