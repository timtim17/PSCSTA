file = open("student_data/population.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    readings = file.readline().strip("\r\n")
    changes = [int(x) for x in file.readline().strip("\r\n").split(" ")]
    del readings
    p = []
    l = len(changes)
    for i in range(1, len(changes) + 1):
        for j in range(0, len(changes), i):
            p.append(sum(changes[j:j + i]))
        if not l % i == 0:
            p.append(sum(changes[-1 - i:-1]))
    print max(p)
