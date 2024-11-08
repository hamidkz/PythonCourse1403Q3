prices = [23, 43, 1, 22]
# max_profit: ? 7

max_profit = 0
min_price = prices[0]

for price in prices:
    min_price = min(price, min_price) # 4
    max_profit = max(max_profit, price - min_price)

print(max_profit)
