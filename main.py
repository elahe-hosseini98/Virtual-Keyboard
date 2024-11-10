import cv2
import os
from virtual_keyboard_creator.keyboard import create_keyboard
from virtual_keyboard_creator.key_pos_dict import generate_key_pos_dict
from virtual_keyboard_creator.pre_load_key_labels import preload_images
from touch_detector.hand_landmark_detection import get_thumb_index_positions
from touch_detector.get_pointed_key import get_pointed_key
from virtual_keyboard_creator.keyboard_logic import logic
from touch_detector.get_selected_key import get_selected_key
from virtual_keyboard_creator.config_key_labels_shifter import upper_config_key_labels, lower_config_key_labels
from time import time


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    width_height_ratio = 16 / 9
    init_width = 640
    init_height = int(init_width / width_height_ratio)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, init_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, init_height)

    cv2.namedWindow('Webcam Feed', cv2.WINDOW_NORMAL)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    key_pos_dict = generate_key_pos_dict(init_width, init_height)

    CAPSLOCK = False

    char_png_path = os.path.join(script_dir, 'statics', 'keys', 'small', 'png')

    preloaded_images = preload_images(char_png_path=char_png_path)

    output_text = ""

    # Open the output file and initialize the last execution time
    with open(r'output/output.txt', 'w') as file:
        file.truncate(0)
        file.write(output_text)

    last_execution_time = time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        pointed_key = None

        window_rect = cv2.getWindowImageRect('Webcam Feed')
        window_width = window_rect[2]
        new_height = int(window_width / width_height_ratio)

        if new_height != init_height or window_width != init_width:
            init_width = window_width
            init_height = new_height
            key_pos_dict = generate_key_pos_dict(init_width, init_height)

        resized_frame = cv2.resize(frame, (window_width, new_height))

        index_pos, thumb_pos, index_thumb_distance = get_thumb_index_positions(resized_frame)

        if index_pos is not None:
            pointed_key = get_pointed_key(key_pos_dict, index_pos)

            if pointed_key is not None and index_thumb_distance is not None:
                selected_key = get_selected_key(pointed_key, index_thumb_distance, dist_threshold=40)
                if selected_key and (time() - last_execution_time) >= 1:
                    output_text, CAPSLOCK = logic(selected_key, output_text, capslock=CAPSLOCK)

                    # Update the content of output.txt
                    with open(r'output/output.txt', 'w') as file:
                        file.write(output_text)

                    if selected_key == 'capslock':
                        if CAPSLOCK:
                            char_png_path = os.path.join(script_dir, 'statics', 'keys', 'capital', 'png')
                            upper_config_key_labels()
                        else:
                            char_png_path = os.path.join(script_dir, 'statics', 'keys', 'small', 'png')
                            lower_config_key_labels()

                        preloaded_images = preload_images(char_png_path=char_png_path)
                        key_pos_dict = generate_key_pos_dict(init_width, init_height)

                    # Update last execution time
                    last_execution_time = time()

            print(f'Pointed Key = {pointed_key}, Output Text = "{output_text}"')

        create_keyboard(resized_frame, key_pos_dict=key_pos_dict, preloaded_images=preloaded_images,
                        pointed_key=pointed_key)

        cv2.resizeWindow('Webcam Feed', window_width, new_height)
        cv2.imshow('Webcam Feed', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
