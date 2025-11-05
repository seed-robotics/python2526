import pygame
import random
import colorsys
pygame.init()

WIDTH, HEIGHT = 800, 300
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smooth Colorful Mouse Trail")

clock = pygame.time.Clock()
running = True

# Surface for fade effect
trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_alpha(25)      # smaller = longer trail
trail_surface.fill((0, 0, 0))    # black fade

hue = 0
# Slightly bigger brush radius
RADIUS = 16

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gradually fade old circles
    win.blit(trail_surface, (0, 0))

    # Draw a colorful circle at mouse position
    pos = pygame.mouse.get_pos()
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    color = tuple(int(c * 255) for c in rgb)
    pygame.draw.circle(win, color, pos, RADIUS)
    hue = (hue + 0.005) % 1  # smooth color cycling

    pygame.display.update()
    clock.tick(120)

pygame.quit()
