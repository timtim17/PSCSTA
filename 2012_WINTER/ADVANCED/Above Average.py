file = open("student_data/average.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    del data[0]
    average = float(sum(data))/len(data)
    above = 0
    for grade in data:
        if grade > average:
            above += 1
    print "%.3f%%" % (float(above)/len(data) * 100)
