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

direction = (0, -20)


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
            if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 20):
                direction = (0, -20)
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -20):
                direction = (0, 20)
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (20, 0):
                direction = (-20, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-20, 0):
                direction = (20, 0)


    #Building and animating assets
    if direction != (0, 0):
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = [head_x + dx, head_y + dy]
        snake.insert(0, new_head)
        snake.pop()

    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))
    
    pygame.display.flip()
    clock.tick(10)