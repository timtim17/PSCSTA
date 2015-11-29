# file = open("data\\histonum.dat")
file = open("D:\\JudgesData\\histonum.dat")

numbers = []

while True:
    data = file.readline().rstrip("\r\n")
    if data == '': break
    numbers.append(data)

numbers = ''.join(numbers)

o = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for number in numbers:
    o[int(number)] += 1

for number in range(len(o)):
    if o[number] == 0: continue
    print ("%d|" % number) + ('*' * o[number]) + ('{%d}' % o[number])