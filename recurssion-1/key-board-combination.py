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


def print_keypad_combination(string):
    if not string:
        return ['']
    first_char = string[0]
    rest_str = string[1:]
    answers = print_keypad_combination(rest_str)
    first_char_choices = list(key_board_map.get(first_char))
    answer_choices = []
    for char in first_char_choices:
        for ans in answers:
            answer_choices.append(char + ans)
    return answer_choices


print(print_keypad_combination('456'))
