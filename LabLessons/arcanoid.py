import pygame
import sys
import paddle as pd
from settings import *
import ball as bl
import brick as br
import heart as h

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
paddle = pygame.Rect(WIDTH// 2- PADDLE_WIDTH//2, HEIGHT-4*PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_DIAMETER, BALL_DIAMETER )
font_big = pygame.font.Font(None, 74)
font = pygame.font.Font(None, 40)
text_over = font_big.render("GAME OVER", True, (255, 255, 0))
text_restart = font.render("Press Space to Restart", True, (255, 0, 0))
rect_over = text_over.get_rect(center=(WIDTH//2, HEIGHT//2))
rect_restart = text_restart.get_rect(center = (WIDTH//2, HEIGHT//2+75))
bricks = br.create_bricks()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ball.x , ball.y = WIDTH//2 , HEIGHT//2
            lives = 3
            bricks = br.create_bricks()
            game_over = False 

    

    for brick in bricks:
        if ball.colliderect(brick["rect"]):
            bricks.remove(brick)
            speed[1] *= -1
    paddle = pd.move_paddle(paddle,PADDLE_SPEED)
    ball = bl.move_ball(ball, paddle)  
    screen.fill(BG_COLOR)
    for brick in bricks:
        pygame.draw.rect(
        screen,
        brick["color"],
        brick["rect"],
        border_radius=10)
    

    if not game_over:
        if ball.y >= HEIGHT:
            lives -= 1
            if lives > 0:
                ball.x , ball.y = WIDTH//2 , HEIGHT//2
            if lives < 0:
                game_over = True
    
    
    
    
    
    
    if game_over:
        screen.fill(BLACK)
        screen.blit(text_over, rect_over)
        screen.blit(text_restart, rect_restart)
        
    else:
        heart_size = 40
        padding =20
        start_x = 10
        start_y = 20
        for i in range(max(0, lives)):
            hx = start_x + i * (heart_size + padding)
            h.draw_heart_parabolic(screen, hx, start_y, heart_size)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

pygame.quit()
sys.exit()




     