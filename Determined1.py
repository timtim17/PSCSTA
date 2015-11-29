# file = open("data\\determined1.dat")
file = open("D:\\JudgesData\\determined1.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    matrix = []
    for j in range(2):
        data = [int(x) for x in file.readline().rstrip("\r\n").split()]
        matrix.append(data)
    print matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
