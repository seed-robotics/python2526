import pygame 
import sys
import random

pygame.init()
HEIGHT,WIDTH = 600,600
CELL = 20
GRID = WIDTH//CELL
FPS = 10
BACKROUND = (0,0,0)
snake = [
[10, 10], # kefali
[9, 10], # swma 1
[8, 10] # oura
]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
food_x = random.randint(0, (WIDTH // CELL) - 1)
food_y = random.randint(0, (HEIGHT // CELL) - 1)
font = pygame.font.Font(None,74) 
font_ui = pygame.font.Font(None,35) 
score = 0
level = 1
highscore = 0                       
def show_game_over():
    screen.fill((0, 0, 0))
    text = font.render("GAME OVER", True, (255, 255, 0))
    rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(2000)
running = True
snake_x,snake_y = 10,10
direction = 'UP'
clock = pygame.time.Clock()
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


    new_head = [snake_x, snake_y]
    snake.insert(0, new_head)
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = 'RIGHT'
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = 'UP'
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = 'DOWN'
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (WIDTH // CELL) - 1)
        food_y = random.randint(0, (HEIGHT // CELL) - 1)
        score += 1
        level = score//5 + 1   

    else:
        snake.pop()
    if snake_x < 0 or snake_x >= GRID or snake_y < 0 or snake_y >= GRID or new_head in snake[1:]:
        show_game_over()
        running = False
        continue
    pygame.draw.rect(screen, (255, 0, 0), (food_x * CELL, food_y * CELL, CELL, CELL))
    for (x, y) in snake:
        pygame.draw.rect(screen, (0, 255, 0), (x * CELL, y * CELL, CELL, CELL))
    
    score_text = font_ui.render(f"Score: {score}", True, (255, 255, 0)) 
    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 5)) 

    level_text = font_ui.render(f"Level: {level}", True, (0, 200, 255)) 
    screen.blit(level_text, (20, 5)) 

    highscore_text = font_ui.render(f"High Score: {highscore}", True, (255, 255, 255)) 
    screen.blit(highscore_text,((WIDTH - highscore_text.get_width()) // 2, 5)) 

    screen.blit(score_text, (WIDTH - score_text.get_width() - 20, 5)) 
    screen.blit(level_text, (20, 5)) 
    screen.blit(highscore_text,((WIDTH - highscore_text.get_width()) // 2, 5))

    pygame.display.flip()


pygame.quit()
sys.exit()