# https://www.youtube.com/watch?v=SiGqwJOvflE&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=36


board = [6, 8, 12, 14, 16]
score = [5, 8, 5, 3, 1]
board_and_score = {
    6: 5,
    8: 8,
    12: 5,
    14: 3,
    16: 1
}
n = 16
gape = 5
dp_arr = [0] * (n + 1)


for i in range(len(dp_arr)):
    if board_and_score.get(i):
        if i - gape >= 0:
            dp_arr[i] = max(dp_arr[i-1], dp_arr[i - gape]+board_and_score.get(i))
    else:
        dp_arr[i] = dp_arr[i-1]

print(dp_arr)