file = open("student_data/dryrun.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    print "I like %s." % data
