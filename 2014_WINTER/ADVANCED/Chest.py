from sys import stdout

file = open("student_data/chest.dat", "r")

lines = int(file.readline().strip("\r\n"))

positions = []

for i in range(lines):
    positions.append(file.readline().strip("\r\n"))

cols = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

rows = {
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
    8: 0
}

for pos in positions:
    board = []
    for i in range(8):
        l = []
        for j in range(8):
            l.append("-")
        board.append(l)
    col = cols[pos[:1]]
    row = rows[int(pos[1:])]
    board[row][col] = "K"

    def replace(col, row):
        if col < 0 or row < 0: return
        try:
            board[row][col] = "?"
        except IndexError: pass

    replace(col + 1, row - 2)
    replace(col - 1, row - 2)
    replace(col + 2, row - 1)
    replace(col - 2, row - 1)

    replace(col + 1, row + 2)
    replace(col - 1, row + 2)
    replace(col + 2, row + 1)
    replace(col - 2, row + 1)

    for row in board:
        for char in row:
            stdout.write(char + " ")
        stdout.write("\n")
    print
