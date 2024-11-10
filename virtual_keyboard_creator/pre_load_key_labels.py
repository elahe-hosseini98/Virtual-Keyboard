import virtual_keyboard.config as config
from PIL import Image
import numpy as np
import os


def preload_images(char_png_path=None):
    images = {}

    for row in config.chars:

        for char in row:
            img_path = os.path.join(char_png_path, f"{char}.png")

            img = Image.open(img_path).convert("RGBA")

            images[char] = np.array(img)

    return images