# Test file for using PyGame to generate a suitable grid for displaying generated dungeon maps
# Richard Horton 2020

import pygame

WIN_SIZE = (255, 255)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(WIN_SIZE)
    clock = pygame.time.Clock()

    for i in range(0, 100):
        pygame.display.update()
        clock.tick(60)
