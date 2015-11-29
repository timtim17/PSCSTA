file = open("student_data/trees.dat", "r")

file.readline().rstrip("\r\n")

forest = {}

while True:
    data = file.readline().rstrip("\r\n")
    if data == '': break
    data = [int(x) for x in data.split(" ")]
    if data[0] not in forest:
        forest[data[0]] = []
    forest[data[0]].append(data[1])

opinions = []

for opinion in forest.values():
    opinion.sort()
    if opinion not in opinions:
        opinions.append(opinion)

print len(opinions)
