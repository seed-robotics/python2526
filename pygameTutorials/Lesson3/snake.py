import pygame
import sys
import random 

def show_game_over():
    screen.fill((0, 0, 0))
    text = font_big.render("GAME OVER", True, (255, 255, 0))
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, rect)
    pygame.display.flip()   

def reset_game():
    global snake_x, snake_y, snake, direction, score, level, FPS, food_x, food_y
    snake_x = 10
    snake_y = 10
    direction = "RIGHT"
    snake = [
        [10, 10],
        [9, 10],
        [8, 10],
        [7, 10],
        [6, 10]
    ]
    score = 0
    level = 1
    FPS = 15
    food_x = random.randint(0, GRID - 1)
    food_y = random.randint(0, GRID - 1)

def handle_game_over():
    show_game_over()
    waiting = True
    while waiting:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                reset_game()
                return

def spawn_super_food():
    global super_food_active, super_food_x, super_food_y, super_food_timer
    super_food_active = True
    super_food_x = random.randint(0, GRID - 1)
    super_food_y = random.randint(0, GRID - 1)
    super_food_timer = SUPER_FOOD_DURATION
def update_super_food():
    global super_food_active, super_food_timer
    if super_food_active:
        super_food_timer -= 1
        if super_food_timer <= 0:
            super_food_active = False
def draw_super_food():
    if super_food_active:
        pygame.draw.rect(
            screen,
            (0, 0, 255),
            (super_food_x * CELL, super_food_y * CELL, CELL, CELL))
def spawn_obstacle():
    global obstacle

    while True:
        ox = random.randint(0, GRID - 2)
        oy = random.randint(0, GRID - 2)

        obstacle = [
            [ox, oy],
            [ox + 1, oy],
            [ox, oy + 1],
            [ox + 1, oy + 1]
        ]

        collision = False
        for cell in obstacle:
            if cell in snake or cell == [food_x, food_y]:
                collision = True
                break

        if not collision:
            break
pygame.init()

try:
    with open("./highscore.txt", "r") as file:
        print("inside")
        highscore = int(file.read().strip())
except:
    highscore = 0

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font_big = pygame.font.Font(None, 74)
font_ui  = pygame.font.Font(None, 30)

super_food_active = False
super_food_x = 0
super_food_y = 0
super_food_timer = 0
SUPER_FOOD_DURATION = 150 
grow=0

obstacle = []

FPS = 15
CELL = 20
GRID = WIDTH//CELL
snake_x = 10
snake_y = 10
direction = "RIGHT"
running = True
score = 0
level = 1
previous_lvl=1
start=1
blink=0
food_x = random.randint(0, (WIDTH // CELL) - 1)
food_y = random.randint(0, (HEIGHT // CELL) - 1)
snake = [
    [10, 10],
    [9, 10],
    [8, 10],
    [7, 10],
    [6, 10]
]
while start:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    blink += 1
    if (blink // 5) % 2 == 0:
        start_text = font_big.render("Press Space to Start", True, (255, 255, 0))
        screen.blit(start_text, ((WIDTH - start_text.get_width())//2, HEIGHT//2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start=0
            break

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    if direction == "LEFT":
        snake_x -= 1
    elif direction == "RIGHT":
        snake_x += 1
    elif direction == "UP":
        snake_y -= 1
    elif direction == "DOWN":
        snake_y += 1

    new_head = [snake_x, snake_y]
    snake.insert(0, new_head)

    if new_head in snake[1:]:
        handle_game_over()
        continue

    if snake_x < 0 or snake_x >= GRID or snake_y < 0 or snake_y >= GRID:
        handle_game_over()
        continue
    if new_head in obstacle:
        handle_game_over()
        continue

    if super_food_active and snake_x == super_food_x and snake_y == super_food_y:
        score += 3
        super_food_active = False
        grow=3

    if (snake_x == food_x and snake_y == food_y):
        score += 1
        grow = 1
        level = score // 5 + 1 
        if level > previous_lvl:
            spawn_obstacle()
        previous_lvl=level
        FPS = 10 + level * 2
        if score > highscore:
            highscore = score
            with open("./highscore.txt", "w") as file:
                file.write(str(highscore))
        food_x = random.randint(0, (WIDTH // CELL) - 1)
        food_y = random.randint(0, (HEIGHT // CELL) - 1)

    if grow == 0:
        snake.pop()
    else:
        grow -= 1
        
    if not super_food_active and random.randint(0, 200) == 0:
        spawn_super_food()
        
    update_super_food()

    screen.fill((0, 0, 0))
    score_text = font_ui.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 5))
    level_text = font_ui.render(f"Level: {level}", True, (0, 200, 255))
    screen.blit(level_text, (20, 5))
    highscore_text = font_ui.render(f"High Score: {highscore}", True, (255, 255, 255))
    screen.blit(highscore_text,((WIDTH - highscore_text.get_width()) // 2, 5))
    draw_super_food()
    pygame.draw.rect(screen,(255, 0, 0),(food_x * CELL, food_y * CELL, CELL, CELL))
    for (x, y) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x * CELL, y * CELL, CELL, CELL))
    for (x, y) in obstacle:
        pygame.draw.rect(
            screen,
            (120, 120, 120),
            (x * CELL, y * CELL, CELL, CELL)
        )
    pygame.display.flip()

pygame.quit()
sys.exit()
