file = open("student_data/overbooked.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    events = []
    file.readline()
    data = file.readline().strip("\r\n").lstrip("(").rstrip(")").split(") (")
    for j in data:
        j = j.split(", ")
        a = [int(x) for x in j[0].split(":")]
        a[0] *= 60
        a = a[0] + a[1]
        b = [int(x) for x in j[1].split(":")]
        b[0] *= 60
        b = b[0] + b[1]
        events.append((a, b))

    events.sort()

    goto = []

    goto.append(events[0])

    for event_index in range(1, len(events)):
        if events[event_index][0] > goto[-1][1]:
            goto.append(events[event_index])

    s = ""
    for event in goto:
        s += "("
        hour = event[0]/60
        minute = event[0] % 60
        s += "%02d:%02d, " % (hour, minute)
        hour = event[1]/60
        minute = event[1] % 60
        s += "%02d:%02d" % (hour, minute)
        s += ") "
    print s
