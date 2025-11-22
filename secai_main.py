#!/usr/bin/env python3
"""
Simple Pygame animation for Raspberry Pi
Runs with X server (startx)
"""

import pygame
import sys
import os

# Don't set framebuffer variables - use X server instead
# These cause "fbcon not available" error on modern Raspberry Pi OS

def main():
    # Initialize pygame
    try:
        pygame.init()
    except Exception as e:
        print(f"Error initializing pygame: {e}")
        sys.exit(1)

    # Get display info
    info = pygame.display.Info()
    print(f"Display resolution: {info.current_w}x{info.current_h}")

    # Create fullscreen display
    try:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        WIDTH, HEIGHT = screen.get_size()
        print(f"Screen size: {WIDTH}x{HEIGHT}")
    except Exception as e:
        print(f"Error creating display: {e}")
        # Fallback to windowed mode
        screen = pygame.display.set_mode((1280, 720))
        WIDTH, HEIGHT = 1280, 720

    pygame.display.set_caption("Simple Animation")

    # Load image with error handling
    image_path = "tin_available.png"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir('.')}")
        pygame.quit()
        sys.exit(1)
    
    try:
        image = pygame.image.load(image_path)
        image_rect = image.get_rect()
        print(f"Image loaded: {image_rect.width}x{image_rect.height}")
    except Exception as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit(1)

    # Starting position
    x_pos = 0
    y_pos = (HEIGHT - image_rect.height) // 2  # center vertically
    speed = 2  # pixels per frame

    # Colors
    BLACK = (0, 0, 0)

    # Main loop
    clock = pygame.time.Clock()
    running = True

    print("Starting animation loop. Press ESC or Q to quit.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

        # Move the image
        x_pos += speed

        # Reset position if it goes off screen
        if x_pos > WIDTH:
            x_pos = -image_rect.width

        # Clear screen
        screen.fill(BLACK)

        # Draw image at new position
        screen.blit(image, (x_pos, y_pos))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(60)  # 60 FPS

    # Clean exit
    pygame.quit()
    print("Animation stopped.")

if __name__ == "__main__":
    main()