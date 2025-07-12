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
Rounds = [
    {
        "name": "Round 1",
        "food_img": "apple.png",
        "points": 100,
        "goal": 300,
        "time": 300
    },

    {
        "name": "Round 2",
        "food_img": "banana.png",
        "points": 20,
        "goal": 750,
        "time": 180
    },

    {
        "name": "Round 3",
        "food_img": "pizza.png",
        "points": 30,
        "goal": 1500,
        "time": 135
    }
]



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
def load_food_image(round_index):
    img_name = Rounds[round_index]["food_img"]
    path = os.path.join(base_path, "assets", img_name)
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, (20, 20))





# ───────── Game State ───────── #
snake = []
direction = (0, 0)
next_direction = (0, 0)
score = 0
current_round_index = 0
round_start_time = pygame.time.get_ticks()
total_score = 0
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

def reset_game(full_reset=False):
    global snake, direction, next_direction, food, score, game_started
    global food_img, round_start_time, total_score, current_round_index
    if full_reset:
        current_round_index = 0
        score = 0
    snake = [[290, 300], [270, 300], [250, 300]]
    direction = (20, 0)
    next_direction = direction
    food = get_random_food_position()
    food_img = load_food_image(current_round_index)
    game_started = False

def round_transition(previous_score):
    screen.fill(BLACK)

    round_name = Rounds[current_round_index]["name"]
    message = f"{round_name} Starting"
    subtext = "Press any key to continue..."
    prev_score = f"Previous Score: {previous_score}"

    msg_text = font.render(message, True, WHITE)
    sub_text = font.render(subtext, True, WHITE)
    score_text = font.render(prev_score, True, WHITE)

    screen.blit(msg_text, (SCREEN_WIDTH // 2 - msg_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(sub_text, (SCREEN_WIDTH // 2 - sub_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    pygame.display.flip()
    pygame.time.delay(2000)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def get_time_left():
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - round_start_time) // 1000
    total_time = Rounds[current_round_index]["time"]
    remaining = max(0, total_time - elapsed_time)
    minutes = remaining // 60
    seconds = remaining % 60
    return f"{minutes:02d}:{seconds:02d}", remaining

def next_round():
    global current_round_index, round_start_time, food_img, score, snake, direction, next_direction, food
    previous_score = score
    current_round_index += 1

    if current_round_index >= len(Rounds):
        result = game_over(screen, win = True)
        if result == 'retry':
            reset_game(full_reset = True)
        else:
            pygame.quit()
            sys.exit()
    else:
        round_transition(previous_score)
        food_img = load_food_image(current_round_index)
        round_start_time = pygame.time.get_ticks()
        food = get_random_food_position()
        snake = [[290, 300], [270, 300], [250, 300]]
        direction = (20, 0)
        next_direction = direction

def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))





# ───────── Initialize Game ───────── #
reset_game(full_reset = True)




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

    # ───── Movement Logic ──── #
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
                reset_game(full_reset = True)
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
                reset_game(full_reset = True)
                continue
            else:
                pygame.quit()
                sys.exit()

        # Food Collision
        head_rect = pygame.Rect(new_head[0], new_head[1], BLOCK_SIZE, BLOCK_SIZE)
        food_rect = pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
        if head_rect.colliderect(food_rect):
            food = get_random_food_position()
            score += Rounds[current_round_index]["points"]
        else:
            snake.pop()

    # ─────── Round Progression ────── #
    time_str, time_left = get_time_left()
    round_goal = Rounds[current_round_index]["goal"]

    if score >= round_goal:
        next_round()
    elif time_left <= 0:
        result = game_over(screen)
        if result == 'retry':
            reset_game(full_reset = True)
        else:
            pygame.quit()
            sys.exit()



    # ───── Drawing ───── #
    screen.fill(BLACK)
    draw_snake()
    screen.blit(food_img, (food[0], food[1]))
    def draw_round_info():
        time_str, _ = get_time_left()
        round_name = Rounds[current_round_index]["name"]
        round_goal = Rounds[current_round_index]["goal"]

        text = font.render(
            f"{round_name} | Total Score: {score} | Goal: {round_goal} | Time: {time_str}",
            True, WHITE
        )
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 10))

    draw_round_info()

    pygame.display.flip()
    clock.tick(FPS)
