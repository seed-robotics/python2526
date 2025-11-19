import pygame
import sys
score1 = 0
score2 = 0
FPS = 120
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.Font(None, 74)
paddle1_speed = 5
paddle2_speed = 5
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_x1 = 50
paddle_y1 = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_x2 = 750
paddle_y2 = HEIGHT // 2 - PADDLE_HEIGHT // 2
BALL_SIZE = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 3
right_score = 0
left_score = 0
ball_speed_y = 4
running = True
while running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         running = False
    screen.fill(BLACK)
    keys = pygame.key.get_pressed() 
    paddle1_rect = pygame.Rect(paddle_x1, paddle_y1, PADDLE_WIDTH, PADDLE_HEIGHT) 
    paddle2_rect = pygame.Rect(paddle_x2, paddle_y2, PADDLE_WIDTH, PADDLE_HEIGHT) 
    ball_rect = pygame.Rect(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)   
    pygame.draw.rect(screen, WHITE, paddle1_rect)
    pygame.draw.rect(screen, WHITE, paddle2_rect)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE // 2)
    score_text = font.render(f"{left_score} {right_score}", True, WHITE)
    text_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_text, text_rect)
    

    if keys[pygame.K_w]:
        paddle_y1 -= paddle1_speed

    if paddle_y1 < 0:
        paddle_y1 = 0

    if paddle_y1 > HEIGHT - PADDLE_HEIGHT:
        paddle_y1 = HEIGHT - PADDLE_HEIGHT

    if keys[pygame.K_s]:
        paddle_y1 += paddle1_speed

    if keys[pygame.K_o]:
        paddle_y2 -= paddle2_speed

    if paddle_y2 < 0:
        paddle_y2 = 0

    if paddle_y2 > HEIGHT - PADDLE_HEIGHT:
        paddle_y2 = HEIGHT - PADDLE_HEIGHT

    if keys[pygame.K_l]:
        paddle_y2 += paddle2_speed

    ball_y += ball_speed_y
    ball_x += ball_speed_x

    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y *= -1


    if paddle1_rect.colliderect(ball_rect):
        ball_speed_x *= -1 
        ball_x = paddle_x1 + PADDLE_WIDTH + BALL_SIZE // 2 

    if paddle2_rect.colliderect(ball_rect):
        ball_speed_x *= -1 
        ball_x = paddle_x2 - PADDLE_WIDTH - BALL_SIZE // 2
    if ball_x < 0:
            right_score += 1
            print(f"Score: {left_score} - {right_score}")
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x *= -1
            continue
    if ball_x > WIDTH:
            left_score += 1
            print(f"Score: {left_score} - {right_score}")
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_speed_x *= -1
            continue
    
   
    pygame.display.flip()
pygame.quit()
sys.exit()