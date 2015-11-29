from math import ceil

file = open("student_data/tiles.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    room = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    area = room[0] * room[1]
    tiles = area + (area * .1)
    print int(ceil(tiles))
