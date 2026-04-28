import pygame
import sys

from settings import WIDTH, HEIGHT, BLACK, FPS
from snake import Snake
from controls import get_direction

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            new_direction = get_direction(event, snake.direction)

            # Only update if direction actually changed
            if new_direction != snake.direction:
                snake.set_direction(new_direction)

    # Update
    snake.move()

    # Draw
    screen.fill(BLACK)
    snake.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)