# https://www.youtube.com/watch?v=HWJ9kIPpzXs&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=31

prices = [300, 15, 8, 24, 3, 5000, 7000, 2, 100]
prices = [1, 2, 3]

last_min = 1
profit = 0

for price in prices:
    last_min = min(last_min, price)
    if price > last_min:
        print(price-last_min)
        profit += price - last_min
        last_min = price

print(profit)