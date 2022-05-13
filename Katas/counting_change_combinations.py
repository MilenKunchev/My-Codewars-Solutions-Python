def count_change(money, coins):
    coins_count = len(coins)
    table = [0] * (money + 1)
    table[0] = 1
    for i in range(0, coins_count):
        coin = coins[i]
        for j in range(coin, money + 1):
            new_value = table[j - coins[i]]
            table[j] += new_value

    return table[money]


print(count_change(4, [1, 2]))  # 1+1+1+1, 1+1+2, 2+2 --> 3
print(count_change(10, [5, 2, 3]))  # 5+5, 5+2+3, 2+2+2+2+2, 3+3+2+2 --> 4
print(count_change(11, [5, 7]))  # 0
