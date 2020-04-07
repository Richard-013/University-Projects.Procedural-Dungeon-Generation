''' Module for generating a data-backed grid to display a map on
    Richard Horton 2020 '''


class Grid:
    ''' Grid class to hold functions and data about the grid the map is
        being display on'''
    def __init__(self, xSize, ySize, displayScreen):
        self.xSize = xSize
        self.ySize = ySize
        self.screen = displayScreen

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
