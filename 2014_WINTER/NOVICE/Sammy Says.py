file = open("student_data/sammysays.dat", "r")

lines = int(file.readline().strip("\r\n"))

commands = []

for i in range(lines):
    commands.append(file.readline().strip("\r\n"))

for command in commands:
    if command[:10] == "Sammy says":
        print command[11:]
