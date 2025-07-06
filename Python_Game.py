import pygame
import sys
import random
import os
from screens import game_over

pygame.init()

base_path = os.path.dirname(__file__)
apple_path = os.path.join(base_path, "assets", "apple.png")

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake.io")

food_img = pygame.image.load(apple_path).convert_alpha()
food_img = pygame.transform.scale(food_img, (20, 20))


snake = [
    [550, 550],
    [550, 530],
    [550, 510],
]


#Color pallete
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


clock = pygame.time.Clock()
snake_block = 10

score = 0
font = pygame.font.SysFont('arial', 28, bold=True)

#food Initialization
food = [random.randrange(0, 600, 20), random.randrange(0, 600, 20)]


#Initializing the directions
dx = 0
dy = 0

direction = (0, 0)
next_direction = direction
game_started = False


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
            if not game_started and event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                game_started = True


        #The Controls for the game
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 20):
                next_direction = (0, -20) 
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -20):
                next_direction = (0, 20)
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (20, 0):
                next_direction = (-20, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-20, 0):
                next_direction = (20, 0)


    #Building and animating assets
    if game_started and next_direction != (0, 0):
        direction = next_direction
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = [head_x + dx, head_y + dy]

        if new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 600:
            result = game_over(screen)
            if result == 'retry':
                # Reset snake and direction
                pygame.time.delay(300)
                snake = [[550, 550], [550, 530], [550, 510]]    
                direction = (0, -20)
                food = [random.randrange(0, 600, 20), random.randrange(0, 600, 20)]
                score = 0
                game_started = False
                continue
            else:
                pygame.quit()
                sys.exit()

        snake.insert(0, new_head)

        if new_head in snake[1:]:
            result = game_over(screen)
            if result == 'retry':
                pygame.time.delay(300)
                snake = [[550, 550], [550, 530], [550, 510]]
                direction = (0, -20)
                next_direction = direction
                food = [random.randrange(0, 600, 20), random.randrange(0, 600, 20)]
                score = 0
                game_started = False
                continue
            else:
                pygame.quit()
                sys.exit()
        
        head_rect = pygame.Rect(new_head[0], new_head[1], snake_block, snake_block)
        food_rect = pygame.Rect(food[0], food[1], 20, 20)

        if head_rect.colliderect(food_rect):
            food = [random.randrange(0, 600, 20), random.randrange(0, 600, 20)]
            score += 1
        else:
            snake.pop()

    screen.fill(BLACK)
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], snake_block, snake_block))
        
    screen.blit(food_img, (food[0], food[1]))
    
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))



    pygame.display.flip()
    clock.tick(10)