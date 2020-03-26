''' Module for generating a dungeon map
    Richard Horton 2020 '''

import Region

class Map:
    ''' Class for generating the overall map of the dungeon
        Takes xSize and ySize as positive integers to define size of the map
        Takes maxArea as a positive integer to set the maximum size of any one room'''
    def __init__(self, xSize, ySize, maxArea):
        self.xSize = xSize
        self.ySize = ySize
        self.maxRegionArea = maxArea
        self.start = Region.Region(0, self.xSize-1, 0, self.ySize-1, self.maxRegionArea)
        self.regions = []
        self.getUsableRegions()

    '''
    Unused Iterative Region Creation - Usable if Recursion Depth is an issue
    def createRegions(self):
        ''''''Creates the specified number of regions using BFS to traverse the dungeon tree''''''
        n = 0
        currentRegion = None
        # Queue of unvisited (unsplit) regions
        unvisited = [self.start]
        # List of visited (split) regions
        visited = []
        while unvisited:
            #if n == 100:
                #break
            # Generate regions
            currentRegion = unvisited.pop(0)
            if currentRegion not in visited:
                currentRegion.createSubRegions()
                if currentRegion.subRegionLeft is not None:
                    unvisited.append(currentRegion.subRegionLeft)
                if currentRegion.subRegionRight is not None:
                    unvisited.append(currentRegion.subRegionRight)
                visited.append(currentRegion)

            n = n + 1

        self.getUsableRegions()'''

    def getUsableRegions(self):
        ''' Traverses the binary tree of the map to find all leaf nodes which
            each represent a usable region'''
        def _findUsableRegions(currentRegion):
            if currentRegion is not None:
                if currentRegion.checkLeaf():
                    self.regions.append(currentRegion)
                _findUsableRegions(currentRegion.subRegionLeft)
                _findUsableRegions(currentRegion.subRegionRight)
        _findUsableRegions(self.start)

if __name__ == "__main__":
    theMap = Map(100, 100, 200)
    #0, 10, 0, 5, 33
    print(theMap.start)
    #theMap.createRegions()
    #theMap.getUsableRegions()
    for region in theMap.regions:
        print((region.lowPoint, region.highPoint))
    print(len(theMap.regions))
