import pygame
import math
from settings import RED

def draw_heart_parabolic(surface, x, y, size, color=RED, samples=64):
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
    outline_color = (max(0, color[0] - 60), max(0, color[1] - 60), max(0, color[2] - 60))
    pygame.draw.aalines(surface, outline_color, True, pts)
    
def draw_heart(surface, x, y, size, color=RED):
    radius = size // 4
    left_center = (x + radius, y + radius)
    right_center = (x + radius*3, y + radius)
    pygame.draw.circle(surface, color, left_center, radius)
    pygame.draw.circle(surface, color, right_center, radius)
    points = [
        (x, y + radius),
        (x + size, y + radius),
        (x + size//2, y + size)
    ]
    pygame.draw.polygon(surface, color, points)