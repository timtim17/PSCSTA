file = open("student_data/dryrun.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    subject = file.readline().rstrip("\r\n")
    print "I like %s." % subject
