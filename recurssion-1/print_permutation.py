
def print_permutation(ans, string):
    if not string:
        print(ans)
    for i in range(1, len(string)+1):
        singe_char = string[i-1]
        rest_str = string[:i-1]+string[i:]
        print_permutation(ans+singe_char, rest_str)


print_permutation('', 'abc')
