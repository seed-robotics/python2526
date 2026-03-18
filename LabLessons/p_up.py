from settings import speed_p

def move_p_up(p_up, paddle, flag):
    p_up.y += speed_p
    if paddle.colliderect(p_up):
        flag = False 
    return p_up, flag
