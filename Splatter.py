# file = open("data\\splatter.dat")
file = open("D:\\JudgesData\\splatter.dat")

lines = int(file.readline().rstrip("\r\n"))

def splat(wall, pos):
    if pos[1] < 0 or pos[0] < 0: return
    try:
        wall[pos[0]][pos[1]] = True
    except IndexError: return

for i in range(lines):
    height, width = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    wall = []
    for j in range(height):
        row = []
        for k in range(width):
            row.append(False)
        wall.append(row)
    splatters = int(file.readline().rstrip("\r\n"))
    for j in range(splatters):
        s = [int(x) for x in file.readline().rstrip("\r\n").split()]
        splat(wall, s)
        splat(wall, [s[0], s[1] + 1])
        splat(wall, [s[0], s[1] + 2])
        splat(wall, [s[0], s[1] - 1])
        splat(wall, [s[0], s[1] - 2])
        splat(wall, [s[0] + 1, s[1]])
        splat(wall, [s[0] + 2, s[1]])
        splat(wall, [s[0] - 1, s[1]])
        splat(wall, [s[0] - 2, s[1]])
        splat(wall, [s[0] + 1, s[1] + 1])
        splat(wall, [s[0] - 1, s[1] + 1])
        splat(wall, [s[0] + 1, s[1] - 1])
        splat(wall, [s[0] - 1, s[1] - 1])
    c = True
    for row in wall:
        for a in row:
            if not a:
                c = False
    if c:
        print "YES"
    else:
        print "NO"
