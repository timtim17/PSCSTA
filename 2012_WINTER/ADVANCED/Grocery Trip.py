file = open("student_data/grocery.dat", "r")
# file = open("judge_data/grocery1.dat", "r")
# file = open("judge_data/grocery2.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

suman = []

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    suman.append(data)

lines = int(file.readline().rstrip("\r\n"))

rajesh = []

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    rajesh.append(data)

for animal in suman:
    if animal in rajesh:
        print "Tomatoes for youza!"
        break
else:
    print "No tomatoes for youza!"
