def logic(selected_key=None, text="", capslock=False):

    if selected_key == 'capslock':
        capslock = not capslock

    elif selected_key == 'space':
        text += ' '

    elif selected_key == 'enter':
        text += '\n'

    elif selected_key == 'del':
        if text != "":
            text = text[:-1]

    elif selected_key in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        text += selected_key

    elif selected_key == 'semicolon':
        text += ';'

    elif selected_key == 'dot':
        text += '.'

    elif selected_key == 'comma':
        text += ','

    return text, capslock
