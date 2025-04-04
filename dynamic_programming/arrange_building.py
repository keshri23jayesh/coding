# https://www.youtube.com/watch?v=0nF-BMYy7tc&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=19

n = 5
ss_0 = 1
ss_1 = 1

for i in range(n+1):
    new_s0 = ss_1
    new_s1 = ss_0 + ss_1
    ss_0 = new_s0
    ss_1 = new_s1

print(ss_0)
print(ss_1)

# if we have to place both side of roads, we need square the number.
# cause both side of the road can be filled by same number of ways.