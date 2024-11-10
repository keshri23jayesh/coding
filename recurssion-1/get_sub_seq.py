

def get_sub_seq(string):
    if not string:
        return ['']

    first_char = string[0]
    rest_str = string[1:]

    substrs = get_sub_seq(rest_str)
    ans = []
    for substr in substrs:
        ans.append(first_char + substr)
        ans.append('' + substr)
    return ans


print(get_sub_seq("abc"))

