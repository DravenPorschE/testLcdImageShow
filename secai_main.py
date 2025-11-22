#!/usr/bin/env python3
"""
Pygame animation for Raspberry Pi with auto-scaling and bouncing
Automatically detects display size, scales image to fit, and bounces horizontally
"""

import pygame
import sys
import os

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
        # Fallback to windowed mode (typical for 3.5" SPI: 480x320)
        screen = pygame.display.set_mode((480, 320))
        WIDTH, HEIGHT = 480, 320

    pygame.display.set_caption("Bouncing Animation")

    # Load image with error handling
    image_path = "/home/secai/files/testLcdImageShow/bisco.bmp"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir('.')}")
        pygame.quit()
        sys.exit(1)
    
    try:
        original_image = pygame.image.load(image_path)
        original_rect = original_image.get_rect()
        print(f"Original image size: {original_rect.width}x{original_rect.height}")
    except Exception as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit(1)

    # Scale image to fit screen (max 40% of screen width/height)
    max_width = int(WIDTH * 0.4)
    max_height = int(HEIGHT * 0.4)
    
    # Calculate scaling factor to maintain aspect ratio
    width_ratio = max_width / original_rect.width
    height_ratio = max_height / original_rect.height
    scale_factor = min(width_ratio, height_ratio)
    
    new_width = int(original_rect.width * scale_factor)
    new_height = int(original_rect.height * scale_factor)
    
    image = pygame.transform.smoothscale(original_image, (new_width, new_height))
    image_rect = image.get_rect()
    print(f"Scaled image size: {new_width}x{new_height}")

    # Starting position (center vertically)
    x_pos = 0
    y_pos = (HEIGHT - image_rect.height) // 2
    speed = 3  # pixels per frame
    direction = 1  # 1 for right, -1 for left

    # Colors
    BLACK = (0, 0, 0)

    # Main loop
    clock = pygame.time.Clock()
    running = True

    print("Starting bouncing animation. Press ESC or Q to quit.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

        # Move the image
        x_pos += speed * direction

        # Bounce when hitting edges
        if x_pos <= 0:
            x_pos = 0
            direction = 1  # Change direction to right
        elif x_pos >= WIDTH - image_rect.width:
            x_pos = WIDTH - image_rect.width
            direction = -1  # Change direction to left

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