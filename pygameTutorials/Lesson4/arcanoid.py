import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (20, 20, 20)

PADDLE_WIDTH = 120
PADDLE_HEIGHT = 16
PADDLE_SPEED = 7

BALL_SIZE = 12
BALL_SPEED_X = 4
BALL_SPEED_Y = -4

ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

y_pos = HEIGHT - PADDLE_HEIGHT - 20
paddle = pygame.Rect(
    WIDTH // 2 - PADDLE_WIDTH // 2, #x
    y_pos,                          #y
    PADDLE_WIDTH,
    PADDLE_HEIGHT
)

ball = pygame.Rect(
        WIDTH // 2 - BALL_SIZE // 2,
        HEIGHT // 2,
        BALL_SIZE,
        BALL_SIZE
    )
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH


    ball.x += ball_vel[0]
    ball.y += ball_vel[1]
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_vel[0] *= -1
    if ball.top <= 0:
        ball_vel[1] *= -1
    
    collision_ball = ball.inflate(-20, -20)

    if collision_ball.colliderect(paddle):
        if ball_vel[1] > 0:
            ball.bottom = paddle.top
            ball_vel[1] *= -1

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, (220, 220, 220), paddle)
    pygame.draw.ellipse(screen, (0, 200, 255), ball)
    pygame.display.flip()

pygame.quit()
sys.exit()
