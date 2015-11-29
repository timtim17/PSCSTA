from math import ceil

# file = open("data\\buoyancy.dat")
file = open("D:\\JudgesData\\buoyancy.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = int(file.readline().rstrip("\r\n"))
    b = data * 0.011
    print int(ceil(0.54/b))
