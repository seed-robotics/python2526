import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# FPS & Clock
FPS = 60
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_x = 50
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 5

# Ball settings
BALL_SIZE = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 4
ball_speed_y = 4

left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)  # Default font, size 74

running = True
while running:
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle_y += paddle_speed

    # Keep paddle inside screen
    if paddle_y < 0:
        paddle_y = 0
    if paddle_y > HEIGHT - PADDLE_HEIGHT:
        paddle_y = HEIGHT - PADDLE_HEIGHT

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball bounce on top and bottom of the screen
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y *= -1

    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_x - BALL_SIZE // 2, ball_y - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    if ball_x < 0:  
        print("Goal for Right Player!")
        right_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x *= -1  # Αλλάζει φορά
        continue  # Πάμε στο επόμενο frame, παραλείπουμε τα άλλα checks

    if ball_x > WIDTH:  
        print("Goal for Left Player!")
        left_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x *= -1
        continue

    if paddle_rect.colliderect(ball_rect):
        ball_speed_x *= -1  # Reverse x-direction
        ball_x = paddle_x + PADDLE_WIDTH + BALL_SIZE // 2  # Push the ball outside the paddle to avoid sticking


    # Clear screen
    screen.fill(BLACK)

    # Draw paddle and ball
    pygame.draw.rect(screen, WHITE, paddle_rect)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE // 2)
    score_text = font.render(f"{left_score}   {right_score}", True, WHITE)
    text_rect = score_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(score_text, text_rect)
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()

