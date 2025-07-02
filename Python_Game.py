import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake.io")


snake = [
    [550, 550],
    [550, 530],
    [550, 510],
]

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


clock = pygame.time.Clock()
snake_block = 10

#Initializing the directions
dx = 0
dy = 0


while True:
    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


        #The Controls for the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                dx, dy = 0, -20
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                dx, dy = 0, 20
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                dx, dy = -20, 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                dx, dy = 20, 0


    #Building and animating assets
    head_x, head_y = snake[0]
    new_head = [head_x + dx, head_y + dy]
    snake.insert(0, new_head)
    snake.pop()
    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))
    
    pygame.display.flip()
    clock.tick(10)