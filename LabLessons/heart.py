import pygame
import math

def draw_heart_parabolic(surface, x, y, size, color=(255, 0, 0), samples=64):
    cx = x + size / 2
    cy = y + size / 2
    base_scale = size / 34.0
    pts = []
    for i in range(samples):
        t = (i / samples) * 2 * math.pi
        tx = 16 * math.sin(t) ** 3
        ty = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        px = cx + tx * base_scale
        py = cy - ty * base_scale
        pts.append((int(px), int(py)))
    pygame.draw.polygon(surface, color, pts)
    outline_color = (max(0, color[0] - 60), max(0, color[1])) 