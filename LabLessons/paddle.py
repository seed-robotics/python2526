import pygame

def move_paddle(paddle,PADDLE_SPEED = 10):  
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED
    return paddle