file = open("student_data/practiceproblem.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    print "Let's play %s!" % data
