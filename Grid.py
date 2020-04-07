''' Module for generating a data-backed grid to display a map on
    Richard Horton 2020 '''


class Grid:
    ''' Grid class to hold functions and data about the grid the map is
        being display on'''
    def __init__(self, xSize, ySize, displayScreen):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen

