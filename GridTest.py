# Test file for using PyGame to generate a suitable grid for displaying generated dungeon maps
# Richard Horton 2020

import pygame

WIN_SIZE = (255, 255)
CELL_WIDTH = 20
CELL_HEIGHT = 20
CELL_MARGIN = 5

def drawGrid(displayScreen, xSize, ySize):
    '''Populates the surface with a grid of squares
       displayScreen - pass in a pygame surface to draw rects on
       xSize - integer size of the grid in the x-direction
       ySize - integer size of the grid in the y-direction'''
    # Loop down the y-axis
    for row in range(0, ySize):
        # Check if first run of loop
        if row == 0:
            y = CELL_MARGIN
        else:
            y = y + CELL_MARGIN + CELL_HEIGHT

        # Loop across the x-axis
        for column in range(0, xSize):
            # Check if first run of loop
            if column == 0:
                x = CELL_MARGIN
            else:
                x = x + CELL_MARGIN + CELL_WIDTH

            # Draw cell
            pygame.draw.rect(displayScreen, (255, 255, 255), [x, y, CELL_HEIGHT, CELL_WIDTH])

def makeGridList(xSize, ySize):
    '''Generates a 2D array/list to store data for the displayed grid
       xSize - integer size of the grid in the x-direction
       ySize - integer size of the grid in the y-direction'''
    gridList = []
    for row in range(0, ySize):
        gridList.append([])
        for column in range(0, xSize):
            cellLoc = str(row) + ", " + str(column)
            gridList[row].append(cellLoc)

    return gridList

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    drawGrid(screen, 10, 10)
    grid = makeGridList(10, 10)

    for i in range(0, 100):
        pygame.display.update()
        clock.tick(60)
