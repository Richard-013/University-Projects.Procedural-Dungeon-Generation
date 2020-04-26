''' Module for generating a data-backed grid to display a map on
    Richard Horton 2020 '''

import pygame
import Map
import AStar

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
        self.roomName = None
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
    def __init__(self, xSize, ySize, displayScreen, pathRender):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen
        self.pathRender = pathRender
        self.gridCells = []
        self.theMap = None
        self.corridors = []
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

    def createMap(self, maxArea, minDimension, dungeonType):
        ''' Creates a map and creates it within the grid'''
        # Generate the map
        self.theMap = Map.Map(self.ySize, self.ySize, maxArea, minDimension, dungeonType)

        # Label the room tiles on the map with the appropriate type
        for curRegion in self.theMap.regions:
            for x in range(curRegion.room.low[0], curRegion.room.high[0]+1):
                for y in range(curRegion.room.low[1], curRegion.room.high[1]+1):
                    self.gridCells[x][y].type = "Interior"
                    self.gridCells[x][y].roomName = curRegion.room.name
                    self.gridCells[x][y].blocked = True
                    if (x, y) == curRegion.room.entrance:
                        self.gridCells[x][y].type = "Entrance"
                        self.gridCells[x][y].blocked = False
                    elif (x, y) == curRegion.room.exit:
                        self.gridCells[x][y].type = "Exit"
                        self.gridCells[x][y].blocked = False
                    else:
                        if x == curRegion.room.low[0]:
                            self.gridCells[x][y].type = "Wall"
                        elif x == curRegion.room.high[0]:
                            self.gridCells[x][y].type = "Wall"
                        if y == curRegion.room.low[1]:
                            self.gridCells[x][y].type = "Wall"
                        elif y == curRegion.room.high[1]:
                            self.gridCells[x][y].type = "Wall"

        if self.pathRender:
            # Connect rooms by corridors
            self.connectRooms()

            for path in self.corridors:
                for x in range(0, self.xSize):
                    for y in range(0, self.ySize):
                        if (x, y) in path:
                            if self.gridCells[x][y].type == "Path":
                                # Mark overlapping pathways/corridors
                                self.gridCells[x][y].type = "Overlap"
                            else:
                                # Mark pathways/corridors
                                self.gridCells[x][y].type = "Path"

        # Draw grid on the screen
        self.drawMap()

    def connectRooms(self):
        ''' Creates corridors between the rooms that were generated'''
        for k in range(len(self.theMap.regions)-1, -1, -1):
            # Set start point of path
            start = self.theMap.regions[k].room.exit

            #if k == len(self.theMap.regions)-1:
                # Attempt to have two connections to the last room
                #end = self.theMap.regions[k-2].room.exit
            #else:
            end = self.theMap.regions[k-1].room.entrance

            navigator = AStar.AStar(self, start, end)
            # Find the path between the two points
            path = navigator.findPath()
            if path != 1:
                # If a path was found, store it
                self.corridors.append(path)

            # Memory clean up
            del navigator

    def drawMap(self):
        ''' Draws the map on a grid of squares'''
        # Fill background grey
        self.screen.fill((10, 10, 10))
        # Set font for displaying room names
        font = pygame.font.Font('freesansbold.ttf', 20)
        # Create list to store rendered room names
        roomNames = []

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
                roomText = None
                # Set colour based on grid list contents
                if self.gridCells[row][column].type == "Interior":
                    # Room interior cell colour
                    self.gridCells[row][column].colour = (200, 200, 200)
                elif self.gridCells[row][column].type == "Wall":
                    # Wall cell colour
                    self.gridCells[row][column].colour = (50, 50, 50)
                    # Get the room name
                    roomName = self.gridCells[row][column].roomName
                    # Check if the current room's name has been rendered
                    if roomName not in roomNames:
                        # Render the room name and make a note of it in the list
                        roomText = font.render(roomName, True, (240, 240, 240))
                        roomNames.append(roomName)
                elif self.gridCells[row][column].type == "Entrance":
                    # Entrance cell colour
                    self.gridCells[row][column].colour = (220, 10, 10)
                elif self.gridCells[row][column].type == "Exit":
                    # Exit cell colour
                    self.gridCells[row][column].colour = (10, 10, 220)
                elif self.gridCells[row][column].type == "Path":
                    # Path cell colour
                    self.gridCells[row][column].colour = (165, 42, 42)
                elif self.gridCells[row][column].type == "Overlap":
                    # Overlapping path cell colour
                    self.gridCells[row][column].colour = (110, 15, 25)
                else:
                    # Empty cell colour
                    self.gridCells[row][column].colour = (10, 10, 10)

                # Draw cell
                renderedCell = pygame.draw.rect(self.screen, self.gridCells[row][column].colour, [x, y, CELL_HEIGHT, CELL_WIDTH])
                # If there is a room name to render, render it on the new cell
                if roomText is not None:
                    roomNameRect = roomText.get_rect(center=(renderedCell.left, renderedCell.top))
                    self.screen.blit(roomText, roomNameRect)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")
    gridA = Grid(100, 100, screen, True)
    gridA.createMap(1000, 15, "Ruin")
    #gridA.connectRooms()
    #print(gridA.corridors)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
