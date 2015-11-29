file = open("student_data/koolaid.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    people = int(file.readline().rstrip("\r\n"))
    people *= 0.5
    large = 0
    med = 0
    small = 0
    while people >= 2:
        large += 1
        people -= 2
    while people >= 1:
        med += 1
        people -= 1
    while people >= 0.5:
        small += 1
        people -= 0.5
    s = ""
    if large > 0:
        s += "%d large " % large
    if med > 0:
        s += "%d medium " % med
    if small > 0:
        s += "%d small" % small
    print s
