import pygame
pygame.init()

# Δημιουργία παραθύρου
win = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Άσκηση 1 – Θέση Ποντικιού")

# Γραμματοσειρά
font = pygame.font.Font(None, 48)

# Ρολόι για σταθερό ρυθμό ανανέωσης
clock = pygame.time.Clock()

running = True
while running:
    # Περιορίζει στα 60 FPS και μετρά χρόνο από το προηγούμενο frame
    clock.tick(60)

    # Έλεγχος γεγονότων (π.χ. πάτημα Χ)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Παίρνουμε τη θέση του ποντικιού
    x, y = pygame.mouse.get_pos()

    # Δημιουργούμε το κείμενο που θα δείχνει τη θέση
    text = font.render(f"Θέση ποντικιού: ({x}, {y})", True, (255, 255, 0))

    # Καθαρίζουμε το φόντο
    win.fill((0, 0, 100))

    # Εμφανίζουμε το κείμενο
    win.blit(text, (50, 120))

    # Ενημέρωση της οθόνης
    pygame.display.update()

pygame.quit()
