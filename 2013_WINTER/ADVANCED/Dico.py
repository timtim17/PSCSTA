file = open("student_data/dico.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    data = [int(x) for x in file.readline().strip("\r\n").split(" ")]
    del data[-1]
    first = data[0]
    del data[0]
    count = 1
    if first == 7 or first == 11 or first == 15 or first == 20:
        print "WIN %d" % count
        continue
    elif first == 2 or first == 3 or first == 10 or first == 13 or first == 19:
        print "LOSS %d" % count
        continue
    for roll in data:
        count += 1
        if roll == 7 or roll == 10 or roll == 11 or roll == 15:
            print "LOSS %d" % count
            break
        elif roll == first:
            print "WIN %d" % count
            break
    else:
        print "NO RESULT %d" % count
