file = open("student_data/cds.dat", "r")

lines = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]

jack = []
jill = []

for i in range(lines[0]):
    data = int(file.readline().rstrip("\r\n"))
    jack.append(data)

for i in range(lines[1]):
    data = int(file.readline().rstrip("\r\n"))
    jill.append(data)

shared = 0

for cd in jack:
    if cd in jill:
        shared += 1

print shared
