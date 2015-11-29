file = open("student_data/climb.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    data = int(file.readline().strip("\r\n"))
    spaces = data - 1
    for i in range(data):
        print (" " * spaces) + ("C" * (data - spaces))
        spaces -= 1
