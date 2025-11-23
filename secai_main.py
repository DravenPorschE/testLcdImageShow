#!/usr/bin/env python3
"""
Pygame animation for Raspberry Pi with auto-scaling and bouncing
Automatically detects display size, scales image to fit, and bounces horizontally
Includes a loading screen with spinning overlay
"""

import os
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_NOMOUSE', '1')

import pygame
import sys
import math

def draw_spinner(surface, center_x, center_y, radius, angle, color=(255, 255, 255), thickness=4):
    """Draw a rotating spinner/loading indicator"""
    # Draw arc segments for spinner effect
    num_segments = 8
    for i in range(num_segments):
        segment_angle = (angle + (i * 360 / num_segments)) % 360
        start_angle = math.radians(segment_angle)
        end_angle = math.radians(segment_angle + 30)
        
        # Calculate alpha based on segment position (fading effect)
        alpha = int(255 * (i / num_segments))
        
        # Draw arc segment
        start_pos = (
            center_x + radius * math.cos(start_angle),
            center_y + radius * math.sin(start_angle)
        )
        end_pos = (
            center_x + radius * math.cos(end_angle),
            center_y + radius * math.sin(end_angle)
        )
        
        # Create color with alpha
        segment_color = (*color[:3], alpha)
        pygame.draw.line(surface, color, start_pos, end_pos, thickness)

def show_loading_screen(screen, WIDTH, HEIGHT, duration=3000):
    """Display loading screen with spinner for specified duration (in milliseconds)"""
    # Colors matching the Android layout
    PINK_BG = (231, 104, 131)  # #E76883
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    angle = 0
    
    # Font for loading text
    font_large = pygame.font.Font(None, int(HEIGHT * 0.1))  # Responsive font size
    font_small = pygame.font.Font(None, int(HEIGHT * 0.06))
    
    print("Showing loading screen...")
    
    while pygame.time.get_ticks() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    return False
        
        # Fill background with pink color
        screen.fill(PINK_BG)
        
        # Draw "Loading..." text
        loading_text = font_large.render("Loading...", True, WHITE)
        loading_rect = loading_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))
        screen.blit(loading_text, loading_rect)
        
        # Draw spinner below text
        spinner_y = HEIGHT // 2 + 20
        draw_spinner(screen, WIDTH // 2, spinner_y, 30, angle, WHITE, 5)
        
        # Draw subtitle
        subtitle_text = font_small.render("Your privacy matters", True, WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        screen.blit(subtitle_text, subtitle_rect)
        
        # Update display
        pygame.display.flip()
        
        # Rotate spinner
        angle = (angle + 10) % 360
        
        # Control frame rate
        clock.tick(60)
    
    print("Loading complete!")
    return True

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
    
    # Show loading screen first
    if not show_loading_screen(screen, WIDTH, HEIGHT, duration=3000):
        pygame.quit()
        return

    # Load image with error handling
    image_path = "/home/secai/files/testLcdImageShow/tin_available.png"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        print(f"Current directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir('.')}")
        pygame.quit()
        sys.exit(1)
    
    try:
        image = pygame.image.load(image_path)
        image_rect = image.get_rect()
        print(f"Image size: {image_rect.width}x{image_rect.height}")
    except Exception as e:
        print(f"Error loading image: {e}")
        pygame.quit()
        sys.exit(1)

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