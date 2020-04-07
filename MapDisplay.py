''' Module for displaying the map on screen
    Richard Horton 2020 '''

import pygame
import Map
import Room
#import Dungeon
#import Old_Dungeon

WIN_SIZE = (1000, 1000)
CELL_WIDTH = 8
CELL_HEIGHT = 8
CELL_MARGIN = 2

class TestGrid:
    ''' Grid class to hold functions and data whilst testing'''
    def __init__(self, xSize, ySize, displayScreen):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen
        self.gridList = self.makeGridList()

    def makeGridList(self):
        ''' Generates a 2D array/list to store data for the displayed grid
            xSize - integer size of the grid in the x-direction
            ySize - integer size of the grid in the y-direction'''
        grid = []
        for row in range(0, self.ySize):
            grid.append([])
            for column in range(0, self.xSize):
                #cellLoc = str(row) + ", " + str(column)
                '''if (column % 5) == 0 and (row % 5) == 0:
                    cellFill = 2
                elif (column % 5) == 0:
                    cellFill = 1
                elif (row % 5) == 0:
                    cellFill = 1
                else:
                    cellFill = 0'''
                cellFill = 0
                grid[row].append(cellFill)

        return grid

    def drawGrid(self):
        ''' Populates the surface with a grid of squares
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
                    colour = (100, 100, 200)
                elif self.gridList[row][column] == 3:
                    colour = (220, 0, 220)
                elif self.gridList[row][column] == 4:
                    colour = (25, 220, 25)
                else:
                    colour = (200, 200, 200)

                # Draw cell
                pygame.draw.rect(self.screen, colour, [x, y, CELL_HEIGHT, CELL_WIDTH])

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = TestGrid(100, 100, screen)
    #print(gridA.gridList)

    #dungeon1 = Old_Dungeon.Dungeon(30, 100, 100)
    #dungeon1.createRegions()
    #dungeon1 = Dungeon.Dungeon(100, 100, 200)

    theMap = Map.Map(100, 100, 750, 15)

    '''for region in theMap.regions:
        print(region)
        print((region.lowPoint, region.highPoint))
        for x in range(region.lowPoint[0], region.highPoint[0]+1):
            for y in range(region.lowPoint[1], region.highPoint[1]+1):
                gridA.gridList[x][y] = 1
                if x == region.lowPoint[0]:
                    gridA.gridList[x][y] = 2
                elif x == region.highPoint[0]:
                    gridA.gridList[x][y] = 2
                if y == region.lowPoint[1]:
                    gridA.gridList[x][y] = 2
                elif y == region.highPoint[1]:
                    gridA.gridList[x][y] = 2'''

    for region in theMap.regions:
        region.room = Room.Room(region.lowPoint, region.highPoint, 15)

    for region in theMap.regions:
        #print(region)
        #print((region.lowPoint, region.highPoint))
        for x in range(region.room.low[0], region.room.high[0]+1):
            for y in range(region.room.low[1], region.room.high[1]+1):
                gridA.gridList[x][y] = 1
                if (x, y) == region.room.entrance:
                    gridA.gridList[x][y] = 3
                elif (x, y) == region.room.exit:
                    gridA.gridList[x][y] = 4
                else:
                    if x == region.room.low[0]:
                        gridA.gridList[x][y] = 2
                    elif x == region.room.high[0]:
                        gridA.gridList[x][y] = 2
                    if y == region.room.low[1]:
                        gridA.gridList[x][y] = 2
                    elif y == region.room.high[1]:
                        gridA.gridList[x][y] = 2

    gridA.drawGrid()

    for i in range(0, 250):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
