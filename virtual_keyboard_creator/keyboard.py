import cv2


def create_keyboard(frame, key_pos_dict=None, preloaded_images=None, pointed_key=None):
    key_bg_color = (90, 90, 90)
    pointed_bg_color = (50, 50, 50)

    for char, (x, y, x_end, y_end) in key_pos_dict.items():
        cv2.rectangle(frame, (x, y), (x_end, y_end), key_bg_color, -1)

        if pointed_key == char:
            cv2.rectangle(frame, (x, y), (x_end, y_end), pointed_bg_color, -1)

        img_np = preloaded_images[char]
        img_height, img_width = img_np.shape[:2]

        img_ratio = min((x_end - x) / img_width, (y_end - y) / img_height)
        resized_img = cv2.resize(img_np, (int(img_width * img_ratio), int(img_height * img_ratio)), interpolation=cv2.INTER_AREA)

        new_width, new_height = resized_img.shape[1], resized_img.shape[0]

        overlay_x = x + (x_end - x - new_width) // 2
        overlay_y = y + (y_end - y - new_height) // 2

        color = resized_img[..., :3]

        alpha = resized_img[..., 3:] / 255.0

        frame[overlay_y:overlay_y + new_height, overlay_x:overlay_x + new_width] = (
            alpha * color + (1 - alpha) * frame[overlay_y:overlay_y + new_height, overlay_x:overlay_x + new_width]
        )

    return frame