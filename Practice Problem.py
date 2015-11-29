file = open("data\\practiceproblem.dat")
# file = open("D:\\JudgesData\\practiceproblem.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    print "Let's play %s!" % data
