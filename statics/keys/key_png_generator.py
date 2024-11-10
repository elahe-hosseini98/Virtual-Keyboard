import os
from PIL import Image
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, 'small', 'jpeg')
output_folder = os.path.join(script_dir, 'small', 'png')

os.makedirs(output_folder, exist_ok=True)

tolerance = 50

max_width, max_height = 0, 0
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.bmp', '.png')):
        img_path = os.path.join(input_folder, filename)
        with Image.open(img_path) as img:
            width, height = img.size
            max_width = max(max_width, width)
            max_height = max(max_height, height)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.bmp', '.png')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGBA")

        new_img = Image.new("RGBA", (max_width, max_height), (255, 255, 255, 255))

        x_offset = (max_width - img.width) // 2
        y_offset = (max_height - img.height) // 2

        new_img.paste(img, (x_offset, y_offset))

        img_array = np.array(new_img)

        white_mask = np.all(np.abs(img_array[:, :, :3] - [255, 255, 255]) <= tolerance, axis=2)

        img_array[~white_mask, :3] = [255, 255, 255]
        img_array[white_mask] = [0, 0, 0, 0]

        processed_img = Image.fromarray(img_array)

        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
        processed_img.save(output_path, format="PNG")

print("All images have been padded, resized, processed, and saved successfully!")
