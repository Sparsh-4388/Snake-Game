import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake.io")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #The Controls for the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Up")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Down")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Left")
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Right")


    
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
sys.quit()