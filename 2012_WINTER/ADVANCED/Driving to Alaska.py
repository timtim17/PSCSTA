file = open("judge_data/drive.dat", "r")

lines = []

while True:
    line = file.readline().rstrip("\r\n")
    if line == '': break
    lines.append(int(line))

del lines[-1]

i = 0
while i < len(lines):
    stations = []
    num_stations = lines[i]
    for j in range(num_stations):
        i += 1
        stations.append(lines[i])
    stations.sort()
    pos = 0
    for station in stations:
        if station <= pos:
            pos = station + 200
            continue
        else:
            print "IMPOSSIBLE"
            break
    else:
        if pos >= 1422:
            print "POSSIBLE"
        else:
            print "IMPOSSIBLE"
    i += 1
