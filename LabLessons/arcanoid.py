import pygame
import sys
import math
import paddle as pd
from settings import *
import ball as bl
import brick as br
import heart

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
paddle = pygame.Rect(WIDTH// 2- PADDLE_WIDTH//2, HEIGHT-4*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_DIAMETER, BALL_DIAMETER )
bricks = br.create_bricks(top_offset=50)
lives = LIVES
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                lives = LIVES
                bricks = br.create_bricks(top_offset=50)
                paddle = pygame.Rect(WIDTH// 2- PADDLE_WIDTH//2, HEIGHT-4*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
                ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_DIAMETER, BALL_DIAMETER )
                speed[0] = BALL_SPEED
                speed[1] = -abs(BALL_SPEED)
                game_over = False
    paddle = pd.move_paddle(paddle,PADDLE_SPEED)
    ball = bl.move_ball(ball, paddle)  
    screen.fill(BG_COLOR)

    if not game_over:
        if ball.y >= HEIGHT:
            lives -= 1
            if lives > 0:
                ball.x = WIDTH // 2
                ball.y = HEIGHT // 2
                speed[0] = BALL_SPEED
                speed[1] = -1*(BALL_SPEED)
            else:
                game_over = True

    for brick in bricks:
        if ball.colliderect(brick["rect"]):
            bricks.remove(brick)
            speed[1] *= -1
        pygame.draw.rect(
        screen,
        brick["color"],
        brick["rect"],
        border_radius=10)
    
    if game_over:
        screen.fill(BLACK)
        msg_surf = font.render("Game Over - Press Space to play again", True, WHITE)
        msg_rect = msg_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(msg_surf, msg_rect)
    else:
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        heart_size = 28
        padding = 10
        start_x = 10
        start_y = 10
        for i in range(max(0, lives)):
            hx = start_x + i * (heart_size + padding)
            heart.draw_heart(screen, hx, start_y, heart_size)
    pygame.display.flip()

pygame.quit()
sys.exit()