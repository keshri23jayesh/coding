# https://www.youtube.com/watch?v=l_nR5X9VmaI&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=13


def coin_change(coins, target):
    dp_arr = [0] * (target + 1)
    dp_arr[0] = 1
    coins = sorted(coins)
    for coin in coins:
        for i in range(coin, len(dp_arr)):
            dp_arr[i] += dp_arr[i-coin]
    print(dp_arr)


coins = [2,3,5]
target = 7
coin_change(coins, target)