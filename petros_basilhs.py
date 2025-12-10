import pygame
import sys
import time

def reset():
    global ball_x
    ball_x = WIDTH // 2
    global ball_y
    ball_y = HEIGHT // 2
    global ball_speed_x
    ball_speed_x += 1
    global ball_speed_y
    ball_speed_y += 1

pygame.init()
clock = pygame.time.Clock()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_SIZE = 15
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 8
ball_speed_y = 8
ability_time = 1
PADDLE_WIDTH, PADDLE_HEIGHT = 25, HEIGHT//5
paddle_x = 50
paddle2_x = WIDTH - paddle_x
paddle_speed = 5
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
running = True

paddle1_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT)
ball_rect = pygame.Rect(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

while running:
    clock.tick(60)
    if score1 >= 50 or score2 >= 50:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    score_text = font.render(f"{score1} {score2}", True, WHITE)
    text_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_text, text_rect)
    paddle1_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    pygame.draw.rect(screen, WHITE, paddle1_rect)
    pygame.draw.rect(screen, WHITE, paddle2_rect)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE // 2)
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y -= paddle_speed
    
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > HEIGHT - PADDLE_HEIGHT:
        paddle_y = HEIGHT - PADDLE_HEIGHT

    if keys[pygame.K_s]:
        paddle_y += paddle_speed

    if keys[pygame.K_e]:
        ball_speed_x=50

    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > HEIGHT + PADDLE_HEIGHT:
        paddle_y = HEIGHT + PADDLE_HEIGHT

    if keys[pygame.K_o]:
        paddle2_y -= paddle_speed
    
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > HEIGHT - PADDLE_HEIGHT:
        paddle2_y = HEIGHT - PADDLE_HEIGHT

    if keys[pygame.K_l]:
        paddle2_y += paddle_speed
    
    if paddle2_y < 0:
        paddle2_y = 0
    if paddle2_y > HEIGHT + PADDLE_HEIGHT:
        paddle2_y = HEIGHT + PADDLE_HEIGHT

    ball_y += ball_speed_y
    ball_x += ball_speed_x

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y =-ball_speed_y
    if ball_x <= 0:
        score2 += 1
        print(f"Score: {score1} - {score2}")
        reset()
        continue

    if ball_x > WIDTH:
        score1 += 1
        print(f"Score: {score1} - {score2}")
        reset()
        continue

    if paddle1_rect.colliderect(ball_rect):
        ball_speed_x *= -1 # Αντιστροφή κατεύθυνσης της μπάλας
        ball_x = paddle_x + PADDLE_WIDTH + BALL_SIZE // 2

    if paddle2_rect.colliderect(ball_rect):
        ball_speed_x *= -1 # Αντιστροφή κατεύθυνσης της μπάλας
        ball_x = paddle2_x - PADDLE_WIDTH - BALL_SIZE // 2
    print(ball_speed_x)
    print(ball_speed_y)
     
pygame.quit()
sys.exit()


    


