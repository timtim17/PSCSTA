file = open("student_data/chaseball.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    length = int(file.readline().strip("\r\n"))
    s = 0
    for i in range(length, 0, -1):
        print (" " * (i - 1)) + "/" + (" " * (2 * s)) + "\\"
        s += 1
    for i in range(length):
        s -= 1
        print (" " * (i)) + "\\" + (" " * (2 * s)) + "/"
    print
