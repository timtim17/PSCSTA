file = open("student_data/conversions.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = [float(x) for x in file.readline().rstrip("\r\n").split(" ")]
    A = data[0]
    B = data[1]
    C = data[2]
    D = data[3]
    del data
    print "%.2f" % ((A/4) + 7 * B)
    print "%.2f" % ((A + B ** 2)/(A + (1/B)) + A/B)
    print "%.2f" % (1/((1/A) - (1/B)))
    print "%.2f" % (4/A/B * ((1 + 5/(C + D))/A) ** 0.5 - A/(C + D))
    print
