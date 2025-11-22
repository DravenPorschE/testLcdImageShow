import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 320, 240   # adjust to your Pi LCD
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Animation")

# Load your image
image = pygame.image.load("tin_available.png")
image_rect = image.get_rect()

# Starting position
x_pos = 0
y_pos = (HEIGHT - image_rect.height) // 2  # center vertically
speed = 2  # pixels per frame

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the image
    x_pos += speed

    # Reset position if it goes off screen
    if x_pos > WIDTH:
        x_pos = -image_rect.width

    # Clear screen
    screen.fill((0, 0, 0))  # black background

    # Draw image at new position
    screen.blit(image, (x_pos, y_pos))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 FPS
