file = open("student_data/gosalmon.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = file.readline().rstrip("\r\n").split(" ")
    if data[0] == data[1]:
        print "PAIR"
    else:
        print "GO SALMON"
