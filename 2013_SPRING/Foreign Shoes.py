file = open("student_data/foreignshoes.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    size = file.readline().rstrip("\r\n").split(" ")
    size[2] = int(size[2])
    if size[0] == "Women":
        if size[1] == "UK":
            print "Women US %d" % (size[2] + 2)
        else:
            print "Women UK %d" % (size[2] - 2)
    else:
        if size[1] == "UK":
            print "Men US %d" % (size[2] + 1)
        else:
            print "Men UK %d" % (size[2] - 1)
