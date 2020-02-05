# Test file for using PyGame to generate a suitable grid for displaying generated dungeon maps
# Richard Horton 2020

import pygame

WIN_SIZE = (1005, 1005)
CELL_WIDTH = 20
CELL_HEIGHT = 20
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
                cellLoc = str(row) + ", " + str(column)
                grid[row].append(cellLoc)

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

                # Draw cell
                pygame.draw.rect(self.screen, (200, 200, 200), [x, y, CELL_HEIGHT, CELL_WIDTH])

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = TestGrid(40, 40, screen)
    gridA.drawGrid()

    for i in range(0, 100):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
