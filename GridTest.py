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
    firstLoopOuter = True
    firstLoopInner = True
    # Loop down the y-axis
    for row in range(0, 10):
        # Check if first run of loop
        if firstLoopOuter:
            y = CELL_MARGIN
            firstLoopOuter = False
        else:
            y = y + CELL_MARGIN + CELL_HEIGHT

        # Loop across the x-axis
        for column in range(0, 10):
            # Check if first run of loop
            if firstLoopInner:
                x = CELL_MARGIN
                firstLoopInner = False
            else:
                x = x + CELL_MARGIN + CELL_WIDTH

            # Draw cell
            pygame.draw.rect(screen, (255, 255, 255), [x, y, CELL_HEIGHT, CELL_WIDTH])

        firstLoopInner = True

    for i in range(0, 100):
        pygame.display.update()
        clock.tick(60)
