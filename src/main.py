from settings import BLACK, WIDTH, HIEGHT
import pygame


pygame.init()

screen = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("Snake Game")

running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    pygame.display.flip()
            

pygame.quit()