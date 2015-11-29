file = open("student_data/powertoluigi.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = list(file.readline().rstrip("\r\n"))
    for char in range(len(data)):
        if data[char] == "M" and data[char + 1] == "a" and data[char + 2] == "r" and data[char + 3] == "i" and data[char + 4] == "o":
            data[char] = "L"
            data[char + 1] = "u"
            data[char + 2] = "i"
            data[char + 3] = "g"
            data[char + 4] = "i"
    print "".join(data)
