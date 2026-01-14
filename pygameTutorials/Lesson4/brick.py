import pygame
from settings import WIDTH

ROW_COLORS = [
    (60, 120, 255),
    (80, 200, 120),
    (255, 200, 80),
    (255, 120, 120),
]

def create_bricks(
    rows=3,
    brick_h=25,
    margin=5,
    top_offset=40
):
    bricks = []

    cols = WIDTH // (80 + margin)
    total_margin = margin * (cols + 1)
    brick_w = (WIDTH - total_margin) // cols
    start_x = (WIDTH - (cols * brick_w + total_margin)) // 2 + margin

    for row in range(rows):
        color = ROW_COLORS[row % len(ROW_COLORS)]

        for col in range(cols):
            x = start_x + col * (brick_w + margin)
            y = top_offset + row * (brick_h + margin)

            brick = {
                "rect": pygame.Rect(x, y, brick_w, brick_h),
                "color": color
            }

            bricks.append(brick)

    return bricks


def draw_bricks(screen, bricks):
    for brick in bricks:
        pygame.draw.rect(
            screen,
            brick["color"],
            brick["rect"],
            border_radius=4
        )


def ball_hits_bricks(ball, velocity, bricks):
    for brick in bricks:
        if ball.colliderect(brick["rect"]):
            bricks.remove(brick)
            velocity[1] *= -1
            break

    return velocity
