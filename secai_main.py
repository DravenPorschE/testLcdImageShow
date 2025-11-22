from PIL import Image
import numpy as np

img = Image.open("tin_available.png").convert("RGB")  # drop alpha
img = img.resize((480, 320))  # optional scale

arr = np.array(img)
r = (arr[:,:,0] >> 3).astype(np.uint16)
g = (arr[:,:,1] >> 2).astype(np.uint16)
b = (arr[:,:,2] >> 3).astype(np.uint16)
rgb565 = (r << 11) | (g << 5) | b

with open("/dev/fb1", "wb") as f:
    f.write(rgb565.tobytes())
