import pygame
pygame.init()

win = pygame.display.set_mode((600, 200))
pygame.display.set_caption("blit() χωρίς μπλοκάρισμα")

font = pygame.font.Font(None, 60)
text1 = font.render("Καλημέρα!", True, (255, 255, 0))
text2 = font.render("Καλώς ήρθες στο Pygame!", True, (0, 255, 0))

clock = pygame.time.Clock()

show_text1 = True
timer = 0
running = True

while running:
    dt = clock.tick(60)  # 60 FPS
    timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Αλλάζουμε μήνυμα κάθε 2 δευτερόλεπτα
    if show_text1 and timer > 2000:
        show_text1 = False
        timer = 0
    elif not show_text1 and timer > 3000:
        show_text1 = True
        timer = 0

    win.fill((0, 0, 100))
    if show_text1:
        win.blit(text1, (180, 70))
    else:
        win.blit(text2, (20, 70))

    pygame.display.update()

pygame.quit()
