''' Module for running A-Star Algorithm on the generated map to connect rooms
    Richard Horton 2020 '''

class AStar():
    ''' Class that holds data and functions for the A-Star algorithm'''
    def __init__(self, currentGrid, start, target):
        # Create lists and grid
        self.grid = currentGrid
        self.openCells = []
        self.closedCells = []
        self.blockedCells = []
        self.currentCell = None

        # Set Movement Costs
        self.horiWeight = 1  # Cost of a horizontal movement
        self.vertiWeight = 1  # Cost of a vertical movement

        # Store start and target co-ordinates
        self.start = start
        self.target = target

        self.resetCells()
        self.markBlockedCells()
        self.setStart()

    def resetCells(self):
        ''' Resets each cell before running the algorithm'''
        for x in range(0, self.grid.xSize):
            for y in range(0, self.grid.ySize):
                thisCell = self.grid.gridCells[x][y]
                thisCell.parent = None
                thisCell.gVal = None
                thisCell.hVal = None
                thisCell.fVal = None

    def setStart(self):
        ''' Sets up current cell's values and adds it to the open cells list'''
        self.currentCell = self.grid.gridCells[self.start[0]][self.start[1]]
        self.currentCell.gVal = 0
        self.currentCell.hVal = self.calcDistance(self.start[0], self.start[1], self.target[0], self.target[1])
        self.currentCell.fVal = self.currentCell.gVal + self.currentCell.hVal
        self.openCells = []
        self.openCells.append(self.currentCell)

    def calcDistance(self, currentX, currentY, targetX, targetY):
        ''' Calculate the distance between two cells'''
        # Distance along X-Axis
        distX = abs(targetX - currentX)
        # Distance along Y-Axis
        distY = abs(targetY - currentY)

        # Return the total distance
        return (distX*self.horiWeight) + (distY*self.vertiWeight)

    def generateValues(self, workingCell):
        ''' Generates f, g, and h values for the given cell pairing, and updates if they
            are more efficient'''
        tempG = self.currentCell.gVal + 1
        tempH = self.calcDistance(workingCell.x, workingCell.y, self.target[0], self.target[1])
        tempF = tempG + tempH
        if workingCell.fVal is None or tempF < workingCell.fVal:
            workingCell.gVal = tempG
            workingCell.hVal = tempH
            workingCell.fVal = tempF
            workingCell.parent = self.currentCell

    def generateNeighbourValues(self):
        ''' Generates the f, g, and h values for neighbouring cells'''
        for workingCell in self.currentCell.neighbourList:
            if workingCell is None or (workingCell.x, workingCell.y) in self.blockedCells:
                continue
            elif workingCell not in self.closedCells:
                self.generateValues(workingCell)

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

    def markBlockedCells(self):
        ''' Places any blocked cells in the closed cells list'''
        for x in range(0, self.grid.xSize):
            for y in range(0, self.grid.ySize):
                if self.grid.gridCells[x][y].blocked is True:
                    # If a cell is marked as blocked, add its coordinates to the blocked cells list
                    self.blockedCells.append((x, y))
                '''elif x == 0 or y == 0:
                    # Prevent pathfinding following the edges of the map
                    self.blockedCells.append((x, y))
                elif x == self.grid.xSize-1 or y == self.grid.ySize-1:
                    # Prevent pathfinding following the edges of the map
                    self.blockedCells.append((x, y))'''

    def findPath(self):
        ''' Finds the path using A*'''
        goalReached = False
        # While there are still possible cells to visit, iterate through them
        while len(self.openCells) > 0:
            self.currentCell = self.openCells[0]
            currentIndex = 0

            # Find the best cell to move to
            for index, cell in enumerate(self.openCells):
                if cell.fVal is None:
                    continue

                if cell.fVal < self.currentCell.fVal:
                    self.currentCell = cell
                    currentIndex = index

            self.openCells.pop(currentIndex)
            self.closedCells.append(self.currentCell)

            # Check if the target cell has been reached
            if self.currentCell.x == self.target[0]:
                if self.currentCell.y == self.target[1]:
                    goalReached = True
                    break

            # Generate values for neighbouring cells
            self.generateNeighbourValues()

            for neighbour in self.currentCell.neighbourList:
                # Skip if the neighbour has already been closed
                if neighbour in self.closedCells or neighbour is None:
                    continue

                if neighbour.fVal is None:
                    continue

                # Add neighbour to the open cells list if it is not present
                if neighbour not in self.openCells:
                    self.openCells.append(neighbour)

        if goalReached:
            # Return the path taken if the goal was reached
            return self.generatePath()
        else:
            # Print message of no possible path if the goal was not found
            return 1

    def generatePath(self):
        ''' Back-tracks through the navigation to the target and generates a followable path'''
        path = []
        thisCell = self.grid.gridCells[self.target[0]][self.target[1]]
        while True:
            path.append((thisCell.x, thisCell.y))
            if(thisCell.x == self.start[0] and thisCell.y == self.start[1]):
                break
            thisCell = thisCell.parent

        path.reverse()
        return path
