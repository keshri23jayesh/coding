# https://www.youtube.com/watch?v=nqrXHJWMeBc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=18



n = 7

s0 = 1
s1 = 1

for i in range(2, 8):
    new_s0 = s1
    new_s1 = s0 + s1
    s0 = new_s0
    s1 = new_s1

print(s0, s1)
