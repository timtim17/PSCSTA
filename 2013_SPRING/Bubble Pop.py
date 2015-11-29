file = open("student_data/bubblepop1.dat")

board = []

for i in range(10):
    board.append(file.readline().rstrip("\r\n"))

lines = int(file.readline().rstrip("\r\n"))

coords = []

for i in range(lines):
    coord = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    coords.append(coord)

def search(char, row, column, came_from):
    if row < 0 or row >= 10 or column < 0 or column >= 10: return 0
    if not board[row][column] == char: return 0
    up = 0
    down = 0
    left = 0
    right = 0
    try:
        if not came_from == "up":
            up = search(char, row - 1, column, "down")
    except IndexError: pass
    try:
        if not came_from == "left":
            left = search(char, row, column - 1, "right")
    except IndexError: pass
    try:
        if not came_from == "down":
            down = search(char, row + 1, column, "up")
    except IndexError: pass
    try:
        if not came_from == "right":
            right = search(char, row, column + 1, "left")
    except IndexError: pass

    return 1 + up + down + left + right

for coord in coords:
    x = search(board[coord[0]][coord[1]], coord[0], coord[1], None)
    if x >= 3:
        print "YES %d" % x
    else:
        print "NO"
