file = open("student_data/attendance.dat", "r")

classes = []

students = 0
tardies = 0
_class = 0

while True:
    _class += 1
    data = file.readline().rstrip("\r\n")
    if data == '': break
    data = [int(x) for x in data.split(" ")]
    students += data[0]
    tardies += data[2]
    classes.append((float(data[1])/data[0], _class))

classes.sort()

print students
print tardies
print classes[0][1]
s = ""
for c in classes:
    s += "%d " % c[1]
print s
