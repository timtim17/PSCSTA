# file = open("data\\bank.dat")
file = open("D:\\JudgesData\\bank.dat")

strings = []

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    string = file.readline().rstrip("\r\n")
    commands = []
    num_commands = int(file.readline().rstrip("\r\n"))
    for j in range(num_commands):
        commands.append(file.readline().rstrip("\r\n").split(" "))
    for command in commands:
        s = string
        if command[0] == "SEARCH":
            try:
                s = s[int(command[1]) - 1:].index(command[2]) + int(command[1])
            except:
                s = -1
        elif command[0] == "DELETE":
            s = list(s)
            del s[int(command[1]) - 1:int(command[1]) - 1 + int(command[2])]
            s = ''.join(s)
        elif command[0] == "REPLACE":
            s = list(s)
            s[int(command[1]) - 1] = ' '.join(command[2:])
            s = "".join(s)
        elif command[0] == "INSERT":
            s = list(s)
            s = s[:int(command[1]) - 1] + [' '.join(command[2:])] + [" "] + s[int(command[1]) - 1:]
            s = "".join(s)
        print s