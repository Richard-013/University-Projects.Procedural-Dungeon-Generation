# Module for displaying the map on screen
# Richard Horton 2020

import pygame

WIN_SIZE = (500, 500)
CELL_WIDTH = 10
CELL_HEIGHT = 10
CELL_MARGIN = 5

class TestGrid:
    '''Grid class to hold functions and data whilst testing'''
    def __init__(self, xSize, ySize, displayScreen):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen
        self.gridList = self.makeGridList()

    def makeGridList(self):
        '''Generates a 2D array/list to store data for the displayed grid
        xSize - integer size of the grid in the x-direction
        ySize - integer size of the grid in the y-direction'''
        grid = []
        for row in range(0, self.ySize):
            grid.append([])
            for column in range(0, self.xSize):
                #cellLoc = str(row) + ", " + str(column)
                if (column % 5) == 0 and (row % 5) == 0:
                    cellFill = 2
                elif (column % 5) == 0:
                    cellFill = 1
                elif (row % 5) == 0:
                    cellFill = 1
                else:
                    cellFill = 0
                grid[row].append(cellFill)

        return grid

    def drawGrid(self):
        '''Populates the surface with a grid of squares
        displayScreen - pass in a pygame surface to draw rects on
        xSize - integer size of the grid in the x-direction
        ySize - integer size of the grid in the y-direction'''
        self.screen.fill((75, 75, 75))
        # Loop down the y-axis
        for row in range(0, self.ySize):
            # Check if first run of loop
            if row == 0:
                y = CELL_MARGIN
            else:
                y = y + CELL_MARGIN + CELL_HEIGHT

            # Loop across the x-axis
            for column in range(0, self.xSize):
                # Check if first run of loop
                if column == 0:
                    x = CELL_MARGIN
                else:
                    x = x + CELL_MARGIN + CELL_WIDTH

                # Set colour based on grid list contents
                if self.gridList[row][column] == 1:
                    colour = (200, 50, 50)
                elif self.gridList[row][column] == 2:
                    colour = (50, 50, 200)
                else:
                    colour = (200, 200, 200)

                # Draw cell
                pygame.draw.rect(self.screen, colour, [x, y, CELL_HEIGHT, CELL_WIDTH])

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = TestGrid(31, 31, screen)
    #print(gridA.gridList)
    gridA.drawGrid()

    for i in range(0, 500):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()