import pygame
import colorsys
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 300
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Long Mouse Trail")

clock = pygame.time.Clock()
exit_game = False

# Create a surface for fading effect
trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_alpha(1)  # Lower = longer trail
trail_surface.fill((0, 0, 0))

prev_pos = None
hue = 0  # For cycling through colors

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

    # Slowly fade the previous frames (makes old trails darker)
    gameWindow.blit(trail_surface, (0, 0))

    # Get mouse position and draw
    pos = pygame.mouse.get_pos()
    if prev_pos is not None:
        # Convert hue (0–1) to RGB (0–255)
        color = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(hue, 1, 1))
        pygame.draw.circle(gameWindow, color, pos, 5)
        hue = (hue + 0.005) % 1  # slowly cycle through rainbow colors

    prev_pos = pos

    pygame.display.update()
    clock.tick(500)

pygame.quit()
