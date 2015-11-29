file = open("student_data/deertags.dat")

tags = {}

while True:
    tag = file.readline().rstrip("\r\n")
    if tag == '': break
    if tag[1:4] in tags.keys():
        tags[tag[1:4]].append(tag[5:])
    else:
        tags[tag[1:4]] = [tag[5:]]

fine = 0
ml = 0
nc = 0
c = 0
b = 0

for tag in tags.values():
    status = tag[-1]
    if not status[:4] == "DEAD":
        fine += 1
    else:
        cause = status[7:]
        if cause == "MOUNTAIN LION":
            ml += 1
        elif cause == "NATURAL CAUSES":
            nc += 1
        elif cause == "COYOTE":
            c += 1
        elif cause == "BEAR":
            b += 1

s = len(tags)
print "ALIVE %d%%" % (float(fine)/s * 100)

cd = [(ml, "MOUNTAIN LION"), (nc, "NATURAL CAUSES"), (c, "COYOTE"), (b, "BEAR")]
cd.sort(None, None, True)
for c in cd:
    print "%s %d%%" % (c[1], float(c[0])/s * 100)
