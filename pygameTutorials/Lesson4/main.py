import pygame
import sys
from settings import *
import paddle as pd
import ball as bl
import brick as br

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

paddle = pd.create_paddle(HEIGHT - PADDLE_HEIGHT - 20)
ball = bl.create_ball()
bricks = br.create_bricks(rows=4)

# speed init 
ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ball_vel = bl.move_ball(ball, ball_vel)
    ball_vel = bl.ball_hits_paddle(ball, ball_vel, paddle)
    ball_vel = br.ball_hits_bricks(ball, ball_vel, bricks)
    
    pd.move_paddle(paddle)

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (220, 220, 220), paddle)
    pygame.draw.ellipse(screen, (0, 200, 255), ball)
    br.draw_bricks(screen, bricks)
    pygame.display.flip()

pygame.quit()
sys.exit()
