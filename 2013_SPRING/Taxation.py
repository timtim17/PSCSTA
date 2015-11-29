file = open("student_data/taxation.dat")

lines = int(file.readline().rstrip("\r\n"))

items = []

for i in range(lines):
    item = file.readline().rstrip("\r\n")
    if item[:2] == "T ":
        items.append((float(item[2:]), True))
    else:
        items.append((float(item), False))

total = 0.00

for item in items:
    if not item[1]:
        total += item[0]
    else:
        total += item[0] + (item[0] * 0.0825)

print "$%.2f" % total
