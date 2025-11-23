import os
import sys
import time
import pygame

# --- CONFIGURATION ---
# 1. Use the specific driver for RPi SPI screens
os.environ['SDL_VIDEODRIVER'] = 'linuxfb'
# 2. Point to the specific framebuffer (SPI is usually fb1)
os.environ['SDL_FBDEV'] = '/dev/fb1'
# 3. Disable mouse to prevent errors
os.environ['SDL_NOMOUSE'] = '1'

def main():
    print("Initializing Pygame Video only...")
    
    # Initialize ONLY display (Avoids ALSA/Audio errors)
    pygame.display.init()
    
    # Get the screen dimensions automatically
    # We use FULLSCREEN so it grabs the correct resolution of /dev/fb1
    try:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        w, h = screen.get_size()
        print(f"Display initialized: {w}x{h}")
    except Exception as e:
        print(f"Fullscreen failed, trying 480x320 fallback. Error: {e}")
        screen = pygame.display.set_mode((480, 320))

    # 1. Fill background with BLACK
    screen.fill((0, 0, 0))

    # 2. Draw RED square (20x20) at (0,0)
    # Color format: (R, G, B) -> (255, 0, 0) is Red
    # Rect format: (x, y, width, height)
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 20, 20))

    # 3. Update the display to show the changes
    pygame.display.flip()
    print("Red square drawn at 0,0. Waiting 10 seconds...")

    # Keep script running for 10 seconds so you can see it
    time.sleep(10)

    # Clean exit
    pygame.quit()
    print("Test complete.")

if __name__ == "__main__":
    main()