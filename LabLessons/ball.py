from settings import BALL_SPEED, WIDTH

def move_ball(ball):
    speed=[BALL_SPEED,BALL_SPEED]
    ball.x += speed[0]
    ball.y += speed[1]
    if ball.x > WIDTH or ball.x < 0:
        speed[0] *= -1
    if ball.y < 0:
        speed[1] *= -1
    return ball
    
