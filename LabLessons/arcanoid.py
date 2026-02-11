import pygame
import sys
import paddle as pd
from settings import * 
import ball as bl
import brick as br

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
paddle = pygame.Rect(WIDTH// 2- PADDLE_WIDTH//2, HEIGHT-4*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_DIAMETER, BALL_DIAMETER )
bricks = br.create_bricks()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle = pd.move_paddle(paddle,PADDLE_SPEED)
    ball = bl.move_ball(ball, paddle)  
    screen.fill(BG_COLOR)
    for brick in bricks:
        pygame.draw.rect(
        screen,
        brick["color"],
        brick["rect"],
        border_radius=10)
    
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

pygame.quit()
sys.exit()




     