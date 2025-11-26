import pygame
import sys
import random 

def show_game_over():
    screen.fill((0, 0, 0))
    text = font.render("GAME OVER", True, (255, 255, 0))
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(2000) 

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)

FPS = 10
CELL = 20
GRID = WIDTH//CELL
snake_x = 10
snake_y = 10
direction = "RIGHT"
running = True
food_x = random.randint(0, (WIDTH // CELL) - 1)
food_y = random.randint(0, (HEIGHT // CELL) - 1)
snake = [
    [10, 10],
    [9, 10],
    [8, 10]
]

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

    if snake_x < 0 or snake_x >= GRID or snake_y < 0 or snake_y >= GRID:
        show_game_over()
        running = False
        continue

    if (snake_x == food_x and snake_y == food_y):
        food_x = random.randint(0, (WIDTH // CELL) - 1)
        food_y = random.randint(0, (HEIGHT // CELL) - 1)
    else:
        snake.pop()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(255, 0, 0),(food_x * CELL, food_y * CELL, CELL, CELL))
    for (x, y) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x * CELL, y * CELL, CELL, CELL))

    pygame.display.flip()

pygame.quit()
sys.exit()

