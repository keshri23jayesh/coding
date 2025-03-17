

string = "abcaabcbda"

lookup = dict()

i = 0
j = 0
max_len = 0

while i <= j < len(string):
    if lookup.get(string[j]):
        i+=1
    else:
        lookup[string[j]] = 1
        j+=1
    max_len = max(max_len, j-i+1)

print(max_len)