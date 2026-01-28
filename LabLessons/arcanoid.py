import pygame
import sys
import paddle as pd
from settings import * 
import ball as bl

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
paddle = pygame.Rect(WIDTH// 2- PADDLE_WIDTH//2, HEIGHT-4*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_DIAMETER, BALL_DIAMETER )

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if paddle.colliderect(ball):
        ball_speed_x *= -1 
        ball_x = paddle + PADDLE_WIDTH + BALL_SIZE // 2 

    paddle = pd.move_paddle(paddle,PADDLE_SPEED)
    ball = bl.move_ball(ball)  
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

pygame.quit()
sys.exit()




     