import pygame
import os

# Point to the SPI screen
os.environ['SDL_FBDEV'] = '/dev/fb1'

try:
    pygame.display.init()
    print("Pygame initialized successfully!")
    print("Driver used:", pygame.display.get_driver())
except pygame.error as e:
    print(f"Failed: {e}")

print("\nAttempting to force specific drivers:")
drivers = ['fbcon', 'directfb', 'linuxfb', 'svgalib', 'kmsdrm', 'dummy']

for driver in drivers:
    os.environ['SDL_VIDEODRIVER'] = driver
    try:
        pygame.display.quit()
        pygame.display.init()
        print(f"SUCCESS with driver: {driver}")
    except pygame.error:
        print(f"Failed with driver: {driver}")