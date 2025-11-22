#!/usr/bin/env python3
import time
import os

# Framebuffer path
fb = "/dev/fb1"

# Your LCD resolution
WIDTH = 480
HEIGHT = 320

# Helper: write a single RGB565 color to the entire screen
def fill_screen(color_565):
    with open(fb, "wb") as f:
        # RGB565 is 2 bytes per pixel
        data = color_565.to_bytes(2, byteorder="little")
        f.write(data * (WIDTH * HEIGHT))

# Standard RGB565 colors
RED    = 0xF800
GREEN  = 0x07E0
BLUE   = 0x001F
WHITE  = 0xFFFF
BLACK  = 0x0000

print("Filling RED")
fill_screen(RED)
time.sleep(2)

print("Filling GREEN")
fill_screen(GREEN)
time.sleep(2)

print("Filling BLUE")
fill_screen(BLUE)
time.sleep(2)

print("Filling WHITE")
fill_screen(WHITE)
time.sleep(2)

print("Filling BLACK")
fill_screen(BLACK)
time.sleep(2)

print("Done.")
