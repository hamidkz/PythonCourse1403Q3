# coins: 1, 5, 10, 20, 50
# money = ?

coins = [50, 20, 10, 5, 1] 
# money: 1
money = 88
result = []
while money > 0:
    for coin in coins: # coin = 1
        no = 0
        while money >= coin: # 1 > 1? Yes
            money = money - coin # money = 0
            no += 1
        result.append([coin, no]) # result: [[50, 1], [20, 1], [1, 3]]

print(result)





