def print_abv(ans, string, count):
    if not string:
        if count == 0:
            print(ans)
        else:
            print(ans + str(count))
        return

    # if ans and count > 0:
    #     ans = str(count) + ans
    #     count = 0

    first_char = string[0]
    rest_str = string[1:]

    if count:
        print_abv(ans + str(count) + first_char, rest_str, 0)
    else:
        print_abv(ans + first_char, rest_str, 0)

    print_abv(ans, rest_str, count+1)


print_abv("", "pep", 0)
