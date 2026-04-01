import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 60)
score = 0
running = True
start_time = pygame.time.get_ticks()
duration = 2
color = random.choice(["green", "red"])
mode = random.choice(["PRESS", "DONT_PRESS", "ALWAYS", "NEVER"])

def draw_timer(surface, center, radius, progress):
    pygame.draw.circle(surface, (80,80,80), center, radius, 6)
    start_angle = -math.pi / 2
    end_angle = start_angle + (2 * math.pi * progress)
    rect = pygame.Rect(0,0,radius*2,radius*2)
    rect.center = center
    pygame.draw.arc(surface, (0,200,255), rect, start_angle, end_angle, 12)

def get_text(mode):
    if mode == "PRESS":
        return "ΠΑΤΑ"
    elif mode == "DONT_PRESS":
        return "ΜΗΝ ΠΑΤΑΣ"
    elif mode == "ALWAYS":
        return "ΠΑΤΑ ΟΤΙ ΚΑΙ ΝΑ ΓΙΝΕΙ"
    else:
        return "ΜΗΝ ΠΑΤΗΣΕΙΣ ΟΤΙ ΚΑΙ ΝΑ ΓΙΝΕΙ"

text = get_text(mode)

button = pygame.Rect(0, 0, 120, 120)
button.center = (WIDTH // 2, HEIGHT // 2)

while running:
    now = pygame.time.get_ticks()
    elapsed = (now - start_time) / 1000
    progress = max(0, 1 - (elapsed / duration))
    
    screen.fill((30, 30, 30))

    if progress <= 0:
        start_time = now
        color = random.choice(["green", "red"])
        mode = random.choice(["PRESS", "DONT_PRESS", "ALWAYS", "NEVER"])
        text = get_text(mode)

    if color == "green":
        pygame.draw.rect(screen, (0,200,0), button)
    else:
        pygame.draw.rect(screen, (200,0,0), button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                if mode == "PRESS":
                    score += 1
                elif mode == "DONT_PRESS":
                    score -= 1
                elif mode == "ALWAYS":
                    score += 1
                elif mode == "NEVER":
                    score -= 2

    score_surface = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_surface, (20,20))
    draw_timer(screen, (WIDTH//2, HEIGHT//2), 200, progress)

    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect(center=(WIDTH//2, 80))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()