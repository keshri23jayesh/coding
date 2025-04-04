# https://www.youtube.com/watch?v=4YjEHmw1MX0&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=30


prices = [300, 15, 8, 24, 3, 5000, 95, 2, 100]


max_profit = 0
max_sell_price_till_date = (0,300)
max_buy_price_till_date = (0,300)


for idx, price in enumerate(prices):
    if max_buy_price_till_date[1] > price:
        max_buy_price_till_date = (idx, price)
    if max_sell_price_till_date[1] < price:
        max_sell_price_till_date = (idx, price)

    if max_sell_price_till_date[1] > max_buy_price_till_date[1] and \
        max_sell_price_till_date[0] > max_buy_price_till_date[0]:
        max_profit = max(max_profit, max_sell_price_till_date[1] - max_buy_price_till_date[1])

print(max_profit)

# approach 2:
min_bpt = 300
max_profit = -1

for price in prices:
    min_bpt = min(price, min_bpt)
    max_profit = max(max_profit, price-min_bpt)

print(max_profit)




