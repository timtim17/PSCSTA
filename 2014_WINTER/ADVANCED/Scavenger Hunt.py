from sys import stdout
file = open("student_data/scavengerhunt.dat", "r")

maze = []

for i in range(8):
    maze.append([int(x) for x in file.readline().strip("\r\n").split(" ")])

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def traverse(node, collection):
    x = node.x
    y = node.y
    collection.append(node)
    if x == 7 and y == 7: return maze[y][x]
    if y == 7: return maze[y][x] + traverse(Node(x + 1, y), collection)
    if x == 7: return maze[y][x] + traverse(Node(x, y + 1), collection)
    ca = []
    cb = []
    a = traverse(Node(x + 1, y), ca)
    b = traverse(Node(x, y + 1), cb)
    if a >= b:
        collection += ca
        m = a
    else:
        collection += cb
        m = b
    return maze[y][x] + m
'''
done = False
coords = [0, 0]
score = 0
stack = []

while not done:
    if coords == [7, 7]: done = True
    score += maze[coords[1]][coords[0]]
    stack.append(list(coords))
    try:
        down = maze[coords[1] + 1][coords[0]]
    except IndexError:
        coords[0] += 1
        continue
    try:
        right = maze[coords[1]][coords[0] + 1]
    except IndexError:
        coords[1] += 1
        continue
    if down > right:
        coords[1] += 1
    else:
        coords[0] += 1
'''
collection = []
score = traverse(Node(0, 0), collection)

for node in collection:
    maze[node.y][node.x] = " "

for row in maze:
    for char in row:
        stdout.write(str(char) + " ")
    stdout.write("\n")

print "%d points collected!" % score
