from string import ascii_uppercase

file = open("student_data/survey.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    data = [int(x) for x in file.readline().strip("\r\n").split(" ")]
    count = 0
    mailboxes = {}
    for i in range(1, data[0] + 1):
        mailboxes[i] = []
    surveys = []
    for i in range(data[1]):
        surveys.append(ascii_uppercase[i])
    for i in range(len(surveys)):
        for j in range(i, len(mailboxes), i + 1):
            mailboxes[j + 1].append(surveys[i])
            count += 1

    l = mailboxes.copy()
    max_num = [[-1], -1]
    for key, value in l.iteritems():
        value = len(value)
        if value > max_num[1]:
            max_num = [[key], value]
        elif value == max_num[1]:
            max_num[0].append(key)
    s = "Box that contains the most surveys: "
    for i in max_num[0]:
        s += str(i) + " "
    print s

    print "Box %d has %d surveys." % (data[1], len(mailboxes[data[1]]))

    only_a = []
    for box in mailboxes:
        if mailboxes[box][0] == "A" and len(mailboxes[box]) == 1:
            only_a.append(box)
    s = "Boxes that contain only survey A: "
    for box in only_a:
        s += str(box) + " "
    print s

    only_3 = []
    for box in mailboxes:
        if len(mailboxes[box]) == 3:
            only_3.append(box)
    s = "Boxes that contain exactly three surveys: "
    for box in only_3:
        s += str(box) + " "
    print s

    print "Total number of surveys stuffed: %d" % count

    print
