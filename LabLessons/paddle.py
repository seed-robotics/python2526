import pygame
from settings import WIDTH

def move_paddle(paddle, PADDLE_SPEED = 10):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED
    #dynamic resizing works
    if paddle.x > WIDTH - paddle.width:
        paddle.x = WIDTH - paddle.width
    if paddle.x < 0:
        paddle.x = 0 
    return paddle