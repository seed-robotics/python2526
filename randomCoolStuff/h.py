import sys, math, pygame
from random import randrange as rr

W = H = 900 
screen = pygame.display.set_mode((W, H))

def cg(c, r, n, o=0):
    while True:
        a = 2*math.pi/n * o
        yield (r*math.cos(a) + c[0], r*math.sin(a) + c[1])
        o = (o + 1)%n

while True:
    if not rr(5):
        screen.fill(0)
    color = rr(256), rr(256), rr(256)
    q = rr(1,100)
    a = cg((rr(W), rr(H)), W/rr(1,5), q*rr(1,10))
    b = cg((rr(W), rr(H)), W/rr(1,5), q*rr(1,10), q*rr(100))
    for i in range(rr(10) * q):
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()
        pygame.draw.aaline(screen, color, next(a), next(b))
        pygame.display.flip()