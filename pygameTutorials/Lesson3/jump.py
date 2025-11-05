import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jump Game")

x, y = 200, 400
width, height = 40, 60
velocity = 5
jumping = False
jump_speed = 12
gravity = 0.6
jump_velocity = jump_speed
ground = 400

run = True
while run:
    pygame.time.delay(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += velocity
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            jump_velocity = jump_speed
    else:
        y -= jump_velocity
        jump_velocity -= gravity
        if y >= ground:
            y = ground
            jumping = False

    win.fill((30, 30, 30))
    pygame.draw.rect(win, (255, 50, 50), (x, y, width, height))
    pygame.display.update()

pygame.quit()
