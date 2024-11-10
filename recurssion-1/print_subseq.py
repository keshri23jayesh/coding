def print_subseq(ans, string):
    if not string:
        print(ans)
        return
    first_str = string[0]
    rest_str = string[1:]
    print_subseq(ans + first_str, rest_str)
    print_subseq(ans + '', rest_str)


print_subseq('', 'abc')
