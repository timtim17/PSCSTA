from math import floor

file = open("student_data/nomopoly.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    property = file.readline().strip("\r\n")
    cost = float(file.readline().strip("\r\n")[1:])
    houses = int(file.readline().strip("\r\n"))
    print "If someone lands on %s, they will owe me $%d." % (property, floor(cost * (1 + 1.25) ** houses))
