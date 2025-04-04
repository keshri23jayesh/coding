# https://www.youtube.com/watch?v=yc0LunmJA1A&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=14


def coin_change_permutations(target, coins):
    dp_arr = [0] * (target + 1)
    dp_arr[0] = 1

    for i in range(len(dp_arr)):
        for coin in coins:
            if coin > i:
                continue
            dp_arr[i] += dp_arr[i-coin]

    print(dp_arr)



coins = [2,3,5, 6]
target = 10
coin_change_permutations(target, coins)
