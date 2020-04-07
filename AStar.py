''' Module for running A-Star Algorithm on the generated map to connect rooms
    Richard Horton 2020 '''

import pygame
import Grid

WIN_SIZE = (1000, 1000)

class AStar():
    ''' Class that holds data and functions for the A-Star algorithm'''
    def __init__(self, currentGrid, start, target):
        # Create lists and grid
        self.grid = currentGrid
        self.openCells = []
        self.closedCells = []
        self.currentCell = None
        
        # Set Movement Costs
        self.diagWeight = 14  # Cost of a diagonal movement
        self.horiWeight = 10  # Cost of a horizontal movement
        self.vertiWeight = 10  # Cost of a vertical movement
        
        # Store start and target co-ordinates
        self.start = start
        self.target = target

        self.setStart()

    def setStart(self):
        ''' Sets up current cell's values and adds it to the open cells list'''
        self.currentCell = self.grid.gridCells[self.start[0]][self.start[1]]
        self.currentCell.gVal = 0
        self.currentCell.hVal = self.calcDistance(self.start[0], self.start[1], self.target[0], self.target[1])
        self.currentCell.fVal = 0
        self.openCells.append(self.currentCell)

    def calcDistance(self, currentX, currentY, targetX, targetY):
        ''' Calculate the distance between two cells'''
        # Distance along X-Axis
        distX = abs(currentX - targetX)
        # Distance along Y-Axis
        distY = abs(currentY - targetY)

        # Return the total distance
        return distX + distY

    def compareNodes(self, cellA, cellB):
        ''' Returns preferred cell'''
        if(cellA.fVal == cellB.fVal):
            return self.compareHVals(cellA, cellB)
        elif(cellA.fVal > cellB.fVal):
            return cellA
        else:
            return cellB

    def compareHVals(self, cellA, cellB):
        ''' Compares cells based on their h-value'''
        if(cellA.hVal == cellB.hVal):
            # If h-values are equal, compare the g-values
            return self.compareGVals(cellA, cellB)
        elif(cellA.hVal > cellB.hVal):
            return cellA
        else:
            return cellB

    def compareGVals(self, cellA, cellB):
        ''' Compares cells based on their g-value'''
        if(cellA.gVal == cellB.gVal or cellA.gVal > cellB.gVal):
            # If Cell A is preferred or the cells are equally preferable, return Cell A
            return cellA
        else:
            # If Cell B is more preferable return Cell B
            return cellB

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = Grid.Grid(100, 100, screen)
    gridA.createMap(750, 15)

    for i in range(0, 250):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
