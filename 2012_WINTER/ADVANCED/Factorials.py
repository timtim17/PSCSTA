file = open("judge_data/factorial.dat", "r")
number = int(file.readline().rstrip("\r\n"))
def factorial(n, total=1):
    if n <= 0: return total
    return factorial(n - 1, total * n)

print factorial(number)
