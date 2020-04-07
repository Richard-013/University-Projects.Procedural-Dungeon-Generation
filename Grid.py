''' Module for generating a data-backed grid to display a map on
    Richard Horton 2020 '''

import pygame

WIN_SIZE = (1000, 1000)
CELL_WIDTH = 8
CELL_HEIGHT = 8
CELL_MARGIN = 2

class Cell():
    ''' Class for an individual cell within the map grid'''
    def __init__(self, x, y):
        # Set co-ordinates of this node
        self.x = x
        self.y = y
        self.parent = None  # Parent on the path found by A-Star
        
        # Data
        self.type = "Empty"
        self.blocked = False
        self.colour = (100, 100, 100)

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

        self.gridCells = []
        self.generateCells()

    def generateCells(self):
        ''' Generate cells column by column'''
        for x in range(0, self.xSize):
            currentColumn = []
            # Populate the column with nodes for each value of X
            for y in range(0, self.ySize):
                currentColumn.append(Cell(x, y))
            # Insert column into grid
            self.gridCells.append(currentColumn)
        self.generateNeighbourCells()

    def generateNeighbourCells(self):
        ''' Assign each cell its neighbours'''
        for x in range(0, self.xSize):
            for y in range(0, self.ySize):
                if x < self.xSize-1:
                    # Add right neighbour if there should be one
                    self.gridCells[x][y].right = self.gridCells[x+1][y]
                    self.gridCells[x][y].neighbourList[0] = self.gridCells[x][y].right

                if y < self.ySize-1:
                    # Add above neighbour if there should be one
                    self.gridCells[x][y].up = self.gridCells[x][y+1]
                    self.gridCells[x][y].neighbourList[1] = self.gridCells[x][y].up

                if x > 0:
                    # Add left neighbour if there should be one
                    self.gridCells[x][y].left = self.gridCells[x-1][y]
                    self.gridCells[x][y].neighbourList[2] = self.gridCells[x][y].left

                if y > 0:
                    # Add below neighbour if there should be one
                    self.gridCells[x][y].down = self.gridCells[x][y-1]
                    self.gridCells[x][y].neighbourList[3] = self.gridCells[x][y].down

        # Fill background grey
        self.screen.fill((75, 75, 75))

        # Loop down the y-axis
        for row in range(0, self.ySize):
            # Check if first run of loop and set y accordingly
            if row == 0:
                y = CELL_MARGIN
            else:
                y = y + CELL_MARGIN + CELL_HEIGHT

            # Loop across the x-axis
            for column in range(0, self.xSize):
                # Check if first run of loop and set x accordingly
                if column == 0:
                    x = CELL_MARGIN
                else:
                    x = x + CELL_MARGIN + CELL_WIDTH

                # Set colour based on grid list contents
                if self.gridCells[row][column].type == "Interior":
                    # Room interior cell colour
                    self.gridCells[row][column].colour = (200, 50, 50)
                elif self.gridCells[row][column].type == "Wall":
                    # Wall cell colour
                    self.gridCells[row][column].colour = (100, 100, 200)
                elif self.gridCells[row][column].type == "Entrance":
                    # Entrance cell colour
                    self.gridCells[row][column].colour = (220, 0, 220)
                elif self.gridCells[row][column].type == "Exit":
                    # Exit cell colour
                    self.gridCells[row][column].colour = (25, 220, 25)
                else:
                    # Empty cell colour
                    self.gridCells[row][column].colour = (200, 200, 200)

                # Draw cell
                pygame.draw.rect(self.screen, self.gridCells[row][column].colour, [x, y, CELL_HEIGHT, CELL_WIDTH])


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = Grid(100, 100, screen)
    gridA.drawGrid()

    for i in range(0, 250):
        pygame.event.get()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
