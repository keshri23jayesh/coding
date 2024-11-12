
def print_encodings(ans, string):
    if not string:
        print(ans)
        return

    print_encodings(ans + chr(int(string[:1])+64), string[1:])
    if len(string) >= 2:
        print_encodings(ans + chr(int(string[:2])+64), string[2:])


print_encodings('', '123')
