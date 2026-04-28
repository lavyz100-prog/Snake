import pygame
from settings import GRID

def get_direction(event, current_direction):
    if event.type == pygame.KEYDOWN:

        if event.key in (pygame.K_UP, pygame.K_w):
            return (0, -GRID)

        if event.key in (pygame.K_DOWN, pygame.K_s, pygame.K_x):
            return (0, GRID)

        if event.key in (pygame.K_LEFT, pygame.K_a):
            return (-GRID, 0)

        if event.key in (pygame.K_RIGHT, pygame.K_d):
            return (GRID, 0)

    return current_direction