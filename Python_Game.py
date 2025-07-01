import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake.io")


snake = [
    [100, 50],
    [80, 50],
    [60, 50],
]

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


clock = pygame.time.Clock()
snake_block = 10


while True:
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


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


    #Building and animating assets
    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))
    
    pygame.display.flip()
    clock.tick(10)