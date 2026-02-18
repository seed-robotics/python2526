from settings import WIDTH
import pygame
ROW_COLORS = [(153,67,67),
              (67,167,76),
              (1,254,243),
              (50,125,90),
              (230,142,70)
              ]

def create_bricks(rows=5, brick_h=30, margin=5,top_offset=40):
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


def handle_ball_collision(ball, bricks, speed):

    for brick in bricks[:]:
        if ball.colliderect(brick["rect"]):
            bricks.remove(brick)
            speed[1] *= -1
            return brick
    return None