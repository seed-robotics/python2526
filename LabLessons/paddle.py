import pygame
from settings import WIDTH, PADDLE_WIDTH

def move_paddle(paddle,PADDLE_SPEED = 10):  
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED
    if paddle.x >  WIDTH - PADDLE_WIDTH:
        paddle.x = WIDTH - PADDLE_WIDTH
    if paddle.x < 0:
        paddle.x = 0 
    return paddle