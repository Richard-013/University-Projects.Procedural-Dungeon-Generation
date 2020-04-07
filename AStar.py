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

    def generateValues(self, workingCell):
        ''' Generates f, g, and h values for the given cell pairing, and updates if they
            are more efficient'''
        tempG = self.calcDistance(workingCell.x, workingCell.y, self.currentCell.x, self.currentCell.y)
        tempH = self.calcDistance(workingCell.x, workingCell.y, self.target[0], self.target[1])
        tempF = tempG + tempH
        if workingCell.fVal is None or tempF < workingCell.fVal:
            workingCell.gVal = tempG
            workingCell.hVal = tempH
            workingCell.fVal = tempF
            workingCell.parent = self.currentCell

    def generateNeighbourValues(self):
        ''' Generates the f, g, and h values for neighbouring cells'''
        goalFound = False
        for workingCell in self.currentCell.neighbourList:
            if workingCell is not None and workingCell not in self.closedCells:
                self.generateValues(workingCell)
                if workingCell.x == self.target[0] and workingCell.y == self.target[0]:
                    goalFound = True
                    break
                elif workingCell not in self.openCells:
                    self.openCells.append(workingCell)
        return goalFound

    def compareNodes(self, cellA, cellB):
        ''' Returns preferred cell'''
        if cellA.fVal == cellB.fVal:
            return self.compareHVals(cellA, cellB)
        elif cellA.fVal > cellB.fVal:
            return cellA
        else:
            return cellB

    def compareHVals(self, cellA, cellB):
        ''' Compares cells based on their h-value'''
        if cellA.hVal == cellB.hVal:
            # If h-values are equal, compare the g-values
            return self.compareGVals(cellA, cellB)
        elif cellA.hVal > cellB.hVal:
            return cellA
        else:
            return cellB

    def compareGVals(self, cellA, cellB):
        ''' Compares cells based on their g-value'''
        if cellA.gVal == cellB.gVal or cellA.gVal > cellB.gVal:
            # If Cell A is preferred or the cells are equally preferable, return Cell A
            return cellA
        else:
            # If Cell B is more preferable return Cell B
            return cellB

    def findPath(self):
        ''' Finds the path using A*'''
        goalReached = False
        # While there are still possible cells to visit, iterate through them
        while(self.openCells):
            if(len(self.openCells) == 1):
                # If there is only one cell available to visit, generate its neighbour values
                self.currentCell = self.openCells.pop(0)
                goalReached = self.generateNeighbourValues()
                self.closedCells.append(self.currentCell)
                if(goalReached):
                    # Break the loop if the goal is found
                    break
            else:
                # If there is more than one available cell, choose the most optimal available
                nextCell = self.openCells[0]
                for j in range(1, len(self.openCells)):
                    if(self.compareNodes(nextCell, self.openCells[j]) == self.openCells[j]):
                        # If the new cell is more optimal, select it
                        nextCell = self.openCells[j]
                print(nextCell)
                # Move to the next cell
                self.currentCell = nextCell
                # Generate new neighbour values and check if goal is reached
                goalReached = self.generateNeighbourValues()
                # Update cell lists
                self.openCells.remove(self.currentCell)
                self.closedCells.append(self.currentCell)

                if(goalReached):
                    # Break the loop if the goal has been reached
                    break

        if(goalReached):
            # Return the path taken if the goal was reached
            print(self.generatePath())
        else:
            # Print message of no possible path if the goal was not found
            print("No Possible Path")

    def generatePath(self):
        ''' Back-tracks through the navigation to the target and generates a followable path'''
        path = []
        thisCell = self.grid.gridCells[self.target[0]][self.target[1]]
        while(True):
            path.append((thisCell.y, thisCell.y))
            thisCell = thisCell.parent
            if(thisCell.x == self.start[0] and thisCell.y == self.start[1]):
                break

        path.reverse()
        return path

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
