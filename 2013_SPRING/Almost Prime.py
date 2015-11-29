file = open("student_data/almostprime.dat")

numbers = []

number = 0

while True:
    try:
        number = int(file.readline().rstrip("\r\n"))
        numbers.append(number)
    except ValueError: break

def factors(n):
    f = []
    for i in range(1, n + 1):
        if n % i == 0:
            f.append(i)
    return f

factor = []

a = 1

while len(factor) < max(numbers):
    p = factors(a)
    if len(p) == 3:
        factor.append(a)
    a += 1

for i in numbers:
    print factor[i - 1]
