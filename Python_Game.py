import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Pygame Window")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
sys.quit()