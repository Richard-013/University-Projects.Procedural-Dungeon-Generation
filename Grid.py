''' Module for generating a data-backed grid to display a map on
    Richard Horton 2020 '''

import pygame

WIN_SIZE = (1000, 1000)
CELL_WIDTH = 8
CELL_HEIGHT = 8
CELL_MARGIN = 2

class Node():
    ''' Class for an individual cell within the map grid'''
    def __init__(self, x, y):
        # Set co-ordinates of this node
        self.x = x
        self.y = y
        self.parent = None  # Parent on the path found by A-Star
        # Neighbours
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.neighbourList = [None, None, None, None]
        # Set-up f,g,h values for A-Star to use
        self.fVal = None  # G + H
        self.gVal = None  # Distance from starting node
        self.hVal = None  # Distance from end node

    def getX(self):
        ''' Gets the x-coordinate of this cell'''
        return self.x

    def getY(self):
        ''' Gets the y-coordinate of this cell'''
        return self.y

    def showNeighbours(self):
        ''' Prints this cell's neighbouring cells'''
        print("Self: (", self.x, ",", self.y, ")")
        print("Up: (", self.up.getX(), ",", self.up.getY(), ")")
        print("Down: (", self.down.getX(), ",", self.down.getY(), ")")
        print("Left: (", self.left.getX(), ",", self.left.getY(), ")")
        print("Right: (", self.right.getX(), ",", self.right.getY(), ")")

class Grid:
    ''' Grid class to hold functions and data about the grid the map is
        being display on'''
    def __init__(self, xSize, ySize, displayScreen):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen

        self.gridNodes = []
        self.generateNodes()

    def generateNodes(self):
        # Generate nodes column by column
        for x in range(0, self.xSize):
            currentColumn = []
            # Populate the column with nodes for each value of X
            for y in range(0, self.ySize):
                currentColumn.append(Node(x, y))
            # Insert column into grid
            self.gridNodes.append(currentColumn)
        self.generateNeighbourNodes()

    def generateNeighbourNodes(self):
        # Assign each node its neighbours
        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                if(x < self.xSize-1):
                    # Add right neighbour if there should be one
                    self.gridNodes[x][y].right = self.gridNodes[x+1][y]
                    self.gridNodes[x][y].neighbourList[0] = self.gridNodes[x+1][y]

                if(y < self.ySize-1):
                    # Add above neighbour if there should be one
                    self.gridNodes[x][y].up = self.gridNodes[x][y+1]
                    self.gridNodes[x][y].neighbourList[1] = self.gridNodes[x][y+1]

                if(x > 0):
                    # Add left neighbour if there should be one
                    self.gridNodes[x][y].left = self.gridNodes[x-1][y]
                    self.gridNodes[x][y].neighbourList[2] = self.gridNodes[x-1][y]

                if(y > 0):
                    # Add below neighbour if there should be one
                    self.gridNodes[x][y].down = self.gridNodes[x][y-1]
                    self.gridNodes[x][y].neighbourList[4] = self.gridNodes[x][y-1]


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = Grid(100, 100, screen)

    for i in range(0, 250):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
