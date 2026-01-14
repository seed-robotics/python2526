import pygame
from settings import WIDTH, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED

def create_paddle(y_pos):
    return pygame.Rect(
        WIDTH // 2 - PADDLE_WIDTH // 2,
        y_pos,
        PADDLE_WIDTH,
        PADDLE_HEIGHT
    )

def move_paddle(paddle):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    # όρια οθόνης
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH
