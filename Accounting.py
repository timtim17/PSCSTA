# file = open("data\\accounting.dat")
file = open("D:\\JudgesData\\accounting.dat")

costs = []

while True:
    price = list(''.join(file.readline().rstrip("\r\n").split(',')))
    if price == []: break
    del price[0]
    if price[0] == '(':
        del price[0]
        del price[-1]
        price = -float(''.join(price))
    else:
        price = float(''.join(price))
    costs.append(price)

print "****." * 8
print "Transaction : Balance".center(35, " ")
balance = 0
def format(cost):
    if cost < 0:
        return "$(%s)" % comma(-cost)
    else:
        return "$%s" % comma(cost)
def comma(cost):
    cost = str(cost)
    pennies = cost[cost.index("."):]
    if len(pennies) == 2:
        pennies += "0"
    cost = cost[:cost.index(".")]
    if len(cost) <= 3:
        return cost + pennies
    else:
        for i in range(len(cost) - 3, 0, -3):
            cost = cost[:i] + "," + cost[i:]
        return cost + pennies
for price in costs:
    balance += price
    print "%18s : %-20s" % (format(price), format(balance))
print "****." * 8
