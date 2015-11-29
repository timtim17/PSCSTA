file = open("student_data/flexjbox.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    box = []
    for j in range(data[0]):
        row = []
        for k in range(data[1]):
            row.append("*")
        box.append(row)
    box[data[2]][data[3]] = "J"
    print "\n".join(["".join(x) for x in box])
    print
