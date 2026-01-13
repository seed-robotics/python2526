import pygame 
import sys
import random

HEIGHT,WIDTH = 600,600
CELL = 20
GRID = WIDTH//CELL
FPS = 10
BACKROUND = (0,0,0)
SUPER_FOOD_DURATION = 50
snake = [
[10, 10], # kefali
[9, 10], # swma 1
[8, 10] # oura
]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
font = pygame.font.Font(None, 40)
font_over = pygame.font.Font(None, 74)
food_x = random.randint(0, (WIDTH // CELL) - 1)
food_y = random.randint(0, (HEIGHT // CELL) - 1)
score = 0
level = 1
previous_lvl=1
highscore = 0
blink=0
grow=0
super_food_active=False
obstacle = []

def draw_obstacle():
    global obstacle
    while True:
        ox = random.randint(0,GRID-2)
        oy = random.randint(0,GRID-2)
        obstacle = [
            [ox, oy],
            [ox + 1, oy],
            [ox, oy + 1],
            [ox + 1, oy + 1]
        ]
        colision = False
        for cell in obstacle:
            if cell in snake or cell == [food_x,food_y]:
                colision = True
                break
        if not colision:
            break
    
def show_game_over():
    screen.fill((0, 0, 0))
    text_go = font_over.render("GAME OVER", True, (255, 255, 0))
    rect = text_go.get_rect(center=(WIDTH//2, HEIGHT//2))
    text_space = font_over.render("Press Space to restart", True, (255, 255, 0))
    rect2 = text_space.get_rect(center=(WIDTH//2, HEIGHT//2+text_space.get_height()))
    screen.blit(text_go, rect)
    screen.blit(text_space, rect2)
    pygame.display.flip()

def reset_game():
    global snake,level,direction, score, snake_x, snake_y,FPS, food_x, food_y
    score = 0
    level = 1 
    direction = "RIGHT"
    snake=[
    [10, 10], # kefali
    [9, 10], # swma 1
    [8, 10] # oura
    ]
    FPS = 15
    food_x = random.randint(0, GRID - 1)
    food_y = random.randint(0, GRID - 1)
    snake_x = 10
    snake_y = 10

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


running = True
snake_x,snake_y = 10,10
direction = 'UP'
clock = pygame.time.Clock()
start=1

try:
    with open("./highscore.txt", "r") as file: 
        highscore = int(file.read().strip())
except:
    highscore=0

while start:
    clock.tick(FPS)
    screen.fill(BACKROUND)
    blink+=1
    if ((blink//5)%2 == 0):
        text = font_over.render("Press Space to start", True, (255, 255, 0))
        rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start=0
            break   

while running : 
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKROUND)
    keys = pygame.key.get_pressed()
    if direction == "LEFT":
        snake_x -= 1
    elif direction == "RIGHT":
        snake_x += 1
    elif direction == "UP":
        snake_y -= 1
    elif direction == "DOWN":
        snake_y += 1

    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = 'RIGHT'
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = 'UP'
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = 'DOWN'
    
    if super_food_active and snake_x == super_food_x and snake_y == super_food_y:
        score += 3
        super_food_active = False
        grow=3

    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (WIDTH // CELL) - 1)
        food_y = random.randint(0, (HEIGHT // CELL) - 1)
        score=score+1
        grow=1
        level = score//5 + 1
        level = score // 5 + 1 
        if level > previous_lvl:
            draw_obstacle()
        previous_lvl=level
        if score > highscore:
            highscore = score
            with open("./highscore.txt", "w") as file:
                file.write(str(highscore))
    if grow>0:
        grow-=1
    else:
        snake.pop()
    new_head = [snake_x, snake_y]
    snake.insert(0, new_head)
    if snake_x < 0 or snake_x > GRID or snake_y < 0 or snake_y > GRID or new_head in snake[1:] or new_head in obstacle:
        handle_game_over()
        continue
    if not super_food_active and random.randint(0, 10) == 0:
        spawn_super_food()

    score_text = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 5))
    level_text = font.render(f"Level: {level}", True, (0, 200, 255))
    screen.blit(level_text, (20, 5))
    highscore_text = font.render(f"High Score: {highscore}", True, (255, 255, 255))
    screen.blit(highscore_text,((WIDTH - highscore_text.get_width()) // 2, 5))

    pygame.draw.rect(screen, (255, 0, 0), (food_x * CELL, food_y * CELL, CELL, CELL))
    update_super_food()
    draw_super_food()
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