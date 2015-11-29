file = open("student_data/interstellartravel.dat", "r")

lines = int(file.readline().strip("\r\n"))

def traverse(map, current, destination, distance, stack):
    if current == destination: return distance
    r = []
    for d in map[current]:
        if d[0] in stack: continue
        try:
            s = list(stack)
            s.append(current)
            r.append(traverse(map, d[0], destination, distance + d[1], s))
        except:
            continue
    return min(r)

for i in range(lines):
    locations = {x: [] for x in file.readline().strip("\r\n").split(" ")}
    paths = int(file.readline().strip("\r\n"))
    for j in range(paths):
        l = file.readline().strip("\r\n").split(" ")
        l[2] = int(l[2])
        locations[l[0]].append((l[1], l[2]))
        locations[l[1]].append((l[0], l[2]))
    locs = file.readline().strip("\r\n").split(" ")
    current = locs[0]
    destination = locs[1]
    del locs
    print "%s to %s: %d" % (current, destination, traverse(locations, current, destination, 0, []))
