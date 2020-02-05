# Test file for using PyGame to generate a suitable grid for displaying generated dungeon maps
# Richard Horton 2020

import pygame

WIN_SIZE = (255, 255)
CELL_WIDTH = 20
CELL_HEIGHT = 20
CELL_MARGIN = 5

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Grid Test")

    for i in range(0, 100):
        pygame.display.update()
        clock.tick(60)
