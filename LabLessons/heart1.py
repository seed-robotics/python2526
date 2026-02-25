import pygame
import sys
from pygame.locals import *

# COLORS
FPS = 30
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

PINK1 = (255, 192, 203)
PINK2 = (255, 105, 180)
PINK3 = (255, 20, 147)
PINK4 = (252, 90, 141)
PINK5 = (209, 0, 86)


def main():
    global DISPLAYSURF, FPSCLOCK
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Heart !!!')
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF.fill(WHITE)

    pygame.mixer.music.load("love.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAYSURF, PINK4, (280, 100, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK5, (280, 130, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK4, (280, 160, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK3, (280, 190, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK2, (280, 220, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK2, (310, 100, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK1, (340, 100, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK5, (370, 100, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK2, (250, 100, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK2, (220, 100, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK4, (190, 100, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK4, (310, 70, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK3, (340, 70, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK4, (250, 70, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK5, (220, 70, 30, 30))

        ###########
        pygame.draw.rect(DISPLAYSURF, PINK4, (310, 130, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK3, (340, 130, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK5, (370, 130, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK4, (250, 130, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK4, (220, 130, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK3, (190, 130, 30, 30))

        ######
        pygame.draw.rect(DISPLAYSURF, PINK3, (250, 160, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK5, (220, 160, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK3, (310, 160, 30, 30))
        pygame.draw.rect(DISPLAYSURF, PINK4, (340, 160, 30, 30))

        #
        pygame.draw.rect(DISPLAYSURF, PINK4, (250, 190, 30, 30))

        pygame.draw.rect(DISPLAYSURF, PINK4, (310, 190, 30, 30))

        pygame.display.update()


if __name__ == "__main__":
    main()