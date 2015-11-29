file = open("student_data/bestnumber.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

searching_for = file.readline().rstrip("\r\n")

numbers = []

for i in range(lines):
    data = file.readline().rstrip("\r\n")
    numbers.append(float(data))

def biggest(numbers, index, total):
    l = len(numbers)
    if index >= l: return total
    t = []
    for i in range(index, l):
        t.append(max(biggest(numbers, i + 1, total * numbers[index]), biggest(numbers, i + 1, total/numbers[index])))
    return max(t)

def smallest(numbers, index, total):
    l = len(numbers)
    if index >= l: return total
    t = []
    for i in range(index, l):
        t.append(min(smallest(numbers, i + 1, total * numbers[index]), smallest(numbers, i + 1, total/numbers[index])))
    return min(t)

if searching_for == 'biggest':
    print biggest(numbers, 1, numbers[0])
else:
    print smallest(numbers, 1, numbers[0])
