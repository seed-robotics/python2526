import pygame
import sys
import random
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
font = pygame.font.Font(None, 36)

powerup = None  # single power-up [rect, type] or None
powerup_end_time = 0
powerup_original_width = None
POWERUP_COLOR = (200, 200, 0)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                bricks = br.create_bricks()
                lives = LIVES
                game_over = False
                paddle.x = WIDTH// 2- PADDLE_WIDTH//2
                paddle.y = HEIGHT-4*PADDLE_HEIGHT
                ball.x = WIDTH//2
                ball.y = HEIGHT//2
                speed[0] = BALL_SPEED
                speed[1] = -BALL_SPEED

    if not game_over:
        paddle = pd.move_paddle(paddle,PADDLE_SPEED)
        ball = bl.move_ball(ball, paddle)
        if ball.y > HEIGHT:
            lives -= 1
            if lives <= 0:
                game_over = True
                speed[0] = 0
                speed[1] = 0
            else:
                paddle.width = PADDLE_WIDTH
                powerup = None
                powerup_end_time = 0
                powerup_original_width = None
                paddle.x = WIDTH// 2- PADDLE_WIDTH//2
                paddle.y = HEIGHT-4*PADDLE_HEIGHT
                ball.x = WIDTH//2
                ball.y = HEIGHT//2
                speed[0] = BALL_SPEED
                speed[1] = -BALL_SPEED

        if powerup is not None:
            powerup[0].y += POWERUP_FALL_SPEED
            if powerup[0].colliderect(paddle):
                powerup_original_width = paddle.width
                if powerup[1] == "grow":
                    new_w = int(paddle.width * PADDLE_GROW)
                    new_w = min(WIDTH, new_w)
                else:
                    new_w = int(paddle.width * PADDLE_SHRINK)
                    new_w = max(MIN_PADDLE_WIDTH, new_w)
                cx = paddle.centerx
                paddle.width = new_w
                paddle.x = max(0, min(WIDTH - paddle.width, cx - paddle.width // 2))
                powerup_end_time = pygame.time.get_ticks() + POWERUP_DURATION_MS
                powerup = None
            elif powerup[0].y > HEIGHT:
                powerup = None

        if powerup_end_time and pygame.time.get_ticks() >= powerup_end_time:
            if powerup_original_width is not None:
                paddle.width = powerup_original_width
                paddle.x = max(0, min(WIDTH - paddle.width, paddle.x))
            powerup_end_time = 0
            powerup_original_width = None
    screen.fill(BG_COLOR)
    
    removed = br.handle_ball_collision(ball, bricks, speed)
    if removed is not None:
        if random.random() < POWERUP_CHANCE and powerup is None:
            pu_type = random.choice(["grow", "shrink"])
            r = removed["rect"]
            pu_rect = pygame.Rect(r.centerx - POWERUP_SIZE//2, r.centery - POWERUP_SIZE//2, POWERUP_SIZE, POWERUP_SIZE)
            powerup = [pu_rect, pu_type]
    for brick in bricks:
        pygame.draw.rect(
        screen,
        brick["color"],
        brick["rect"],
        border_radius=10)

    if powerup is not None:
        pygame.draw.rect(screen, POWERUP_COLOR, powerup[0])    
    
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    lives_surf = font.render(f'Lives: {lives}', True, WHITE)
    screen.blit(lives_surf, (10, 10))

    if game_over:
        go_font = pygame.font.Font(None, 48)
        go_surf = go_font.render('GAME OVER - Press SPACE to restart', True, WHITE)
        go_rect = go_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(go_surf, go_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()




     