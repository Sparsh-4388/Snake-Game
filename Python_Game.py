import pygame
import sys
import random
import os
from screens import game_over



# ───────── Constants ───────── #
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
MARGIN = 30
FPS = 10



# ───────── Color Palette ───────── #
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRID_COLOR = (40, 40, 40)



# ───────── Pygame Setup ───────── #
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake.io")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 28, bold=True)





# ───────── Load Assets ───────── #
base_path = os.path.dirname(__file__)
apple_path = os.path.join(base_path, "assets", "apple.png")

food_img = pygame.image.load(apple_path).convert_alpha()
food_img = pygame.transform.scale(food_img, (BLOCK_SIZE, BLOCK_SIZE))




# ───────── Game State ───────── #
snake = []
direction = (0, 0)
next_direction = (0, 0)
score = 0
food = []
game_started = False




# ───────── Helper Functions ───────── #
def get_random_food_position():
    min_pos = MARGIN
    max_pos = SCREEN_WIDTH - MARGIN - BLOCK_SIZE
    return [
        random.randrange(min_pos, max_pos + BLOCK_SIZE, BLOCK_SIZE),
        random.randrange(min_pos, max_pos + BLOCK_SIZE, BLOCK_SIZE)
    ]

def reset_game():
    global snake, direction, next_direction, food, score, game_started
    snake = [[290, 300], [270, 300], [250, 300]]
    direction = (20, 0)
    next_direction = direction
    food = get_random_food_position()
    score = 0
    game_started = False

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))





# ───────── Initialize Game ───────── #
reset_game()




# ───────── Game Loop ───────── #
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if not game_started and event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
                                                  pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d):
                game_started = True

            # Movement Controls
            if event.key in (pygame.K_UP, pygame.K_w) and direction != (0, 20):
                next_direction = (0, -BLOCK_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != (0, -BLOCK_SIZE):
                next_direction = (0, BLOCK_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != (BLOCK_SIZE, 0):
                next_direction = (-BLOCK_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != (-BLOCK_SIZE, 0):
                next_direction = (BLOCK_SIZE, 0)

    # ───── Movement Logic ───── #
    if game_started and next_direction != (0, 0):
        direction = next_direction
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = [head_x + dx, head_y + dy]

        # Wall Collision
        if new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
            result = game_over(screen)
            if result == 'retry':
                pygame.time.delay(300)
                reset_game()
                continue
            else:
                pygame.quit()
                sys.exit()

        # Self Collision
        snake.insert(0, new_head)
        if new_head in snake[1:]:
            result = game_over(screen)
            if result == 'retry':
                pygame.time.delay(300)
                reset_game()
                continue
            else:
                pygame.quit()
                sys.exit()

        # Food Collision
        head_rect = pygame.Rect(new_head[0], new_head[1], BLOCK_SIZE, BLOCK_SIZE)
        food_rect = pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
        if head_rect.colliderect(food_rect):
            food = get_random_food_position()
            score += 1
        else:
            snake.pop()




    # ───── Drawing ───── #
    screen.fill(BLACK)
    draw_snake()
    screen.blit(food_img, (food[0], food[1]))
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)
