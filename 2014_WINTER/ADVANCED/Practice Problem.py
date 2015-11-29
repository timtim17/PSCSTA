file = open("student_data/practiceproblem.dat", "r")

lines = int(file.readline())

for i in range(lines):
    data = file.readline().strip("\r\n")
    print "Let's play %s!" % data
