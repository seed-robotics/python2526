import pygame
pygame.init()

win = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Διαφορά με και χωρίς clock")

clock = pygame.time.Clock()



x = 50
y=50
xspeed = 5
yspeed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += xspeed
    y += yspeed
    if x > 800 or x < 0:
        xspeed = -xspeed
    if y>300 or y<0:
        yspeed = -yspeed
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (0, 200, 255), (x, y), 30)
    pygame.display.update()

    clock.tick(60) #Αλλάζει το πόσο γρήγορα θα τρέχει το πρόγραμμα. Δοκιμάστε να το αλλάξετε. 

pygame.quit()
