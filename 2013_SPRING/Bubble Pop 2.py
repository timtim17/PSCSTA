from sys import stdout

file = open("student_data/bubblepop2.dat")

board = []

for i in range(10):
    board.append(list(file.readline().rstrip("\r\n")))

lines = int(file.readline().rstrip("\r\n"))

coords = []

bubbles = []

for i in range(lines):
    coord = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    coords.append(coord)

def search(char, row, column, came_from):
    if row < 0 or row >= 10 or column < 0 or column >= 10: return 0
    if not board[row][column] == char: return 0
    bubbles.append((row, column))
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

def gravity():
    for i in range(len(board) - 1):
        xs = []
        for c in range(len(board[i + 1])):
            if board[i + 1][c] == "X":
                xs.append(c)
        for j in xs:
            k = i
            while k >= 0:
                t = board[k][j]
                board[k][j] = board[k + 1][j]
                board[k + 1][j] = t
                k -= 1

for coord in coords:
    bubbles = []
    x = search(board[coord[0]][coord[1]], coord[0], coord[1], None)
    if x >= 3:
        for bubble in bubbles:
            board[bubble[0]][bubble[1]] = "X"
    gravity()

v = []
for row in range(len(board)):
    for char in range(len(board[row])):
        if not board[row][char] == "X":
            v.append(search(board[row][char], row, char, None))

if max(v) <= 2:
    print "GAME OVER"

print

for row in board:
    for char in row:
        stdout.write(char)
    stdout.write("\n")
