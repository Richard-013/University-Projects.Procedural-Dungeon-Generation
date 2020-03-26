''' Module for generating regions within a given map
    Richard Horton 2020 '''

from random import randint

class Region:
    '''Class for holding all data on a given region of the map
       Takes co-ordinates of two points as separate positive integers
       maxArea should be a positive integer to match the attribute of the parent Map'''
    def __init__(self, x1, x2, y1, y2, maxArea):
        self.minDimension = 3 # All regions must be at least 3x3
        self.maxArea = maxArea
        self.lowPoint = [0, 0]
        self.highPoint = [0, 0]
        self.setLowHigh(x1, x2, y1, y2)

        self.subRegionLeft = None
        self.subRegionRight = None

        self.createSubRegions()

    def setLowHigh(self, x1, x2, y1, y2):
        '''Sorts co-ordinates into low and high points of region'''
        if(x1 > x2 or x1 == x2):
            self.highPoint[0] = x1
            self.lowPoint[0] = x2
        else:
            self.highPoint[0] = x2
            self.lowPoint[0] = x1

        if(y1 > y2 or y1 == y2):
            self.highPoint[1] = y1
            self.lowPoint[1] = y2
        else:
            self.highPoint[1] = y2
            self.lowPoint[1] = y1

    def checkLeaf(self):
        '''Checks to see if this region is a leaf on the Binary Tree of the map'''
        if self.subRegionLeft is None:
            if self.subRegionRight is None:
                return True
            else:
                return False
        else:
            return False

    def checkArea(self):
        '''Checks if a region is large enough to be split further'''
        xLength = (self.highPoint[0] - self.lowPoint[0]) + 1
        yLength = (self.highPoint[1] - self.lowPoint[1]) + 1
        if xLength >= 3 and yLength >= 3:
            area = xLength * yLength
            if area > self.maxArea:
                return True
            else:
                return False
        else:
            return False

    def checkValidSplit(self, splitPoint, axis):
        '''Checks that a split will not create too small a region'''
        length = self.highPoint[axis] - splitPoint
        if length >= self.minDimension:
            length = splitPoint - self.lowPoint[axis]
            if length >= self.minDimension:
                return True
            else:
                return False
        else:
            return False

    def createSubRegions(self):
        '''Splits the region into two sub-regions if it is large enough'''
        if self.checkArea():
            # Region is large enough to split
            if self.highPoint[0] - self.lowPoint[0] > self.highPoint[1] - self.lowPoint[1]:
                # If region is large in X than in Y
                for i in range(0, 100):
                    # Generate new split point until a valid one is found or 100 have been tried
                    splitPoint = randint(self.lowPoint[0], self.highPoint[0]) # Split on X-Axis
                    if self.checkValidSplit(splitPoint, 0):
                        break
                    
                if not self.checkValidSplit(splitPoint, 0):
                    # If no valid split point was found, do not split
                    return 1
                self.subRegionLeft = Region(self.lowPoint[0], splitPoint, self.lowPoint[1], self.highPoint[1], self.maxArea)
                self.subRegionRight = Region(splitPoint+1, self.highPoint[0], self.lowPoint[1], self.highPoint[1], self.maxArea)
            else:
                for i in range(0, 100):
                    # Generate new split point until a valid one is found or 100 have been tried
                    splitPoint = randint(self.lowPoint[0], self.highPoint[0]) # Split on X-Axis
                    if self.checkValidSplit(splitPoint, 1):
                        break
                
                if not self.checkValidSplit(splitPoint, 1):
                    # If no valid split point was found, do not split
                    return 1
                self.subRegionLeft = Region(self.lowPoint[0], self.highPoint[0], self.lowPoint[1], splitPoint, self.maxArea)
                self.subRegionRight = Region(self.lowPoint[0], self.highPoint[0], splitPoint+1, self.highPoint[1], self.maxArea)

if __name__ == "__main__":
    region = Region(0, 50, 0, 50, 500)
    region.createSubRegions()
    print(region.subRegionLeft)
    print(region.subRegionRight)
