file = open("student_data/dryrun.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    data = file.readline().strip("\r\n")
    print "I wish I were a %s." % data
