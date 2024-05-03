import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_SPEED = 5
PADDLE_SPEED = 7

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create the paddles and ball
paddle_width, paddle_height = 10, 100
player_paddle = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ai_paddle = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)
ball_speed_x = random.choice((BALL_SPEED, -BALL_SPEED))
ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Move the AI paddle
    if ball.y < ai_paddle.y + ai_paddle.height // 2 and ai_paddle.top > 0:
        ai_paddle.y -= PADDLE_SPEED
    elif ball.y > ai_paddle.y + ai_paddle.height // 2 and ai_paddle.bottom < HEIGHT:
        ai_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_speed_x = random.choice((BALL_SPEED, -BALL_SPEED))
        ball_speed_y = random.choice((BALL_SPEED, -BALL_SPEED))

    # Clear the screen
    screen.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, ai_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
