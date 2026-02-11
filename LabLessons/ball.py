from settings import WIDTH, speed

def move_ball(ball, paddle):
    ball.x += speed[0]
    ball.y += speed[1]
    if ball.x > WIDTH or ball.x < 0:
        speed[0] *= -1
    if ball.y < 0:
        speed[1] *= -1
    if paddle.colliderect(ball):
        speed[1] *= -1
        ball.y -= 10   
    return ball


