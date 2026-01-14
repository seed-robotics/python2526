import pygame
from settings import WIDTH, HEIGHT, BALL_SIZE

def create_ball():
    return pygame.Rect(
        WIDTH // 2 - BALL_SIZE // 2,
        HEIGHT // 2,
        BALL_SIZE,
        BALL_SIZE
    )

def move_ball(ball, velocity):
    ball.x += velocity[0]
    ball.y += velocity[1]
    if ball.left <= 0 or ball.right >= WIDTH:
        velocity[0] *= -1
    if ball.top <= 0:
        velocity[1] *= -1
    return velocity

def ball_hits_paddle(ball, velocity, paddle):
    collision_ball = ball.inflate(-4, -4)

    if not collision_ball.colliderect(paddle):
        return velocity

    if velocity[1] > 0:
        ball.bottom = paddle.top
        velocity[1] *= -1

    return velocity

