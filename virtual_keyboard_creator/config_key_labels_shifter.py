import virtual_keyboard.config as config

def lower_config_key_labels():
    config.chars = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'semicolon'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'dot', 'comma'],
        ['capslock', 'space', 'enter', 'del']
    ]

def upper_config_key_labels():
    config.chars = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'semicolon'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', 'dot', 'comma'],
        ['capslock', 'space', 'enter', 'del']
    ]
