''' Module for running A-Star Algorithm on the generated map to connect rooms
    Richard Horton 2020 '''

import pygame
import Grid

WIN_SIZE = (1000, 1000)

class AStar():
    ''' Class that holds data and functions for the A-Star algorithm'''
    def __init__(self, currentGrid, startX, startY, targetX, targetY):
        self.grid = currentGrid
        self.openNodes = []
        self.closedNodes = []
        self.currentNode = None
        # Set Movement Costs
        self.diagWeight = 14  # Cost of a diagonal movement
        self.horiWeight = 10  # Cost of a horizontal movement
        self.vertiWeight = 10  # Cost of a vertical movement
        # Store start and target co-ordinates
        self.startX = startX
        self.startY = startY
        self.targetX = targetX
        self.targetY = targetY
        self.setStart()

    def setStart(self):
        ''' Sets up current node's values and adds it to the open nodes list'''
        self.currentNode = self.grid.gridNodes[self.startX][self.startY]
        self.currentNode.gVal = 0
        self.currentNode.hVal = self.calcDistance(self.startX, self.startY, self.targetX, self.targetY)
        self.currentNode.fVal = 0
        self.openNodes.append(self.currentNode)

    def calcDistance(self, currentX, currentY, targetX, targetY):
        ''' Calculate the distance between two nodes'''
        # Distance along X-Axis
        distX = abs(currentX - targetX)
        # Distance along Y-Axis
        distY = abs(currentY - targetY)

        # Return the total distance
        return distX + distY

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
