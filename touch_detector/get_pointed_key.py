def get_pointed_key(key_pos_dict, index_pos):
    index_x, index_y = index_pos

    for key, (x1, y1, x2, y2) in key_pos_dict.items():
        if x1 <= index_x <= x2 and y1 <= index_y <= y2:

            return key

    return None
