from math import sqrt

file = open("student_data/gorf.dat", "r")

lines = int(file.readline())

for i in range(lines):
    data = file.readline().strip("\r\n")
    a = 0
    b = 0
    c = 0
    temp = ["", 0]
    for j in data:
        if j == " ":
            if temp[1] == 0:
                a = float(temp[0])
                temp[1] = 2
            else:
                b = float(temp[0])
            temp[0] = ""
        else:
            temp[0] += j
    c = float(temp[0])
    del temp
    print round(((-b - sqrt(b ** 2 - 4 * a * c))/(2 * a)) - ((-b + sqrt(b ** 2 - 4 * a * c))/(2 * a)), 1)
