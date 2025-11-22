import os
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')  # or /dev/fb0 if fb1 doesn't exist
os.putenv('SDL_NOMOUSE', '1')

import pygame
import sys

# Initialize only the display module
pygame.display.init()
pygame.font.init()  # optional if you use fonts

# Fullscreen mode for framebuffer
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

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
