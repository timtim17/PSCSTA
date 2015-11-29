file = open("student_data/tacks.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

players = []

for i in range(lines):
    data = file.readline().rstrip("\r\n").split(" ")
    data[1] = int(data[1])
    players.append((data[1], data[0]))

players.sort()

print "%s wins with %d tacks." % (players[-1][1], players[-1][0])
