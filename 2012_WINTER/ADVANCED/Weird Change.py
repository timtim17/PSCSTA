from math import floor

file = open("student_data/weirdChange.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

def exact_change(cost, coins, used=[]):
    if len(coins) == 0: return used
    p = []
    c = cost
    for i in range(len(coins)):
        x = int(floor(cost/coins[i]))
        cost -= (x * coins[i])
        a = exact_change(cost, coins[i + 1:], used + [(coins[i], x)])
        p.append(a)
        cost = c
    m = None
    for i in p:
        coin_sum = 0
        for coin in i:
            coin_sum += coin[1]
        if m is None or m[1] > coin_sum:
            m = (i, coin_sum)
    return m[0]

coins = [47, 37, 23, 13, 5, 1]

for i in range(lines):
    cost = int(file.readline().rstrip("\r\n"))
    us_cost = cost * 0.03

    x = exact_change(cost, coins)
    s = "$%.2f " % us_cost
    for coin in coins:
        for a in x:
            if coin == a[0]:
                s += "%d " % a[1]
                break
        else:
            s += "0 "
    print s
