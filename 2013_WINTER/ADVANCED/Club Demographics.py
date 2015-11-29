file = open("student_data/demographics.dat", "r")

lines = int(file.readline().strip("\r\n"))

club = []

for i in range(lines):
    data = file.readline().strip("\r\n").split()
    del data[0]
    data[1] = float(data[1])
    club.append(data)

ages = []
for member in club:
    ages.append(member[1])

young = min(ages)

youngest = club[ages.index(young)]

print "%s: %.1f" % (youngest[0], youngest[1])
