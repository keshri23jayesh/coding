key_board_map = {
    '1': 'abc',
    '2': 'def',
    '3': 'ghi',
    '4': 'jkl',
    '5': 'mnop',
    '6': 'qrst',
    '7': 'uv',
    '8': 'wxyz',
    '9': '.;',
    '0': '?.',
}


def print_keypad_combination(ans, string):
    if not string:
        print(ans)
        return
    first_char = string[0]
    rest_str = string[1:]
    first_char_options = list(key_board_map.get(first_char))
    for char in first_char_options:
        print_keypad_combination(char + ans, rest_str)


print_keypad_combination('', '40')
