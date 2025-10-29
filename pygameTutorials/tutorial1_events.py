import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Detect All Mouse Motion")

exit_game = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        elif event.type == pygame.MOUSEMOTION:
            # event.pos gives the current position (x, y)
            # event.rel gives the change since the last motion (dx, dy)
            print(f"Mouse moved to {event.pos}, relative movement: {event.rel}")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse button {event.button} pressed at {event.pos}")

        elif event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse button {event.button} released at {event.pos}")

pygame.quit()
