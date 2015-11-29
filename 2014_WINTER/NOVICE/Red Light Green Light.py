file = open("student_data/redlightgreenlight.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = [float(x) for x in file.readline().rstrip("\r\n").split(" ")]
    print "%.2f" % (data[0] * data[1])
