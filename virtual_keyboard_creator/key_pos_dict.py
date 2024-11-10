#from virtual_keyboard.config import chars
import virtual_keyboard.config as config


def generate_key_pos_dict(current_width, current_height):
    key_pos_dict = {}

    key_width = int(current_width * 0.09)
    key_height = int(current_height * 0.09)

    spacing = int(current_width * 0.008)

    start_y = int(current_height * 0.05)

    for row_index, row in enumerate(config.chars):
        row_length = len(row)

        start_x = (current_width - (row_length * key_width + (row_length - 1) * spacing)) // 2

        y = start_y + row_index * (key_height + spacing)

        for char_index, char in enumerate(row):
            x = start_x + char_index * (key_width + spacing)
            key_pos_dict[char] = (x, y, x + key_width, y + key_height)

    return key_pos_dict