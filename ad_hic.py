
s = "hello"
sum = 0
for idx in range(len(s)-1):
    sum += abs(ord(s[idx]) - ord(s[idx + 1]))
print(sum)