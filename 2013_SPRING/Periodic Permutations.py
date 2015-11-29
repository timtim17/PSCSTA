file = open("student_data/periodic2.dat")

elements = []

for i in range(4):
    row = file.readline().rstrip("\r\n").split(" ")
    for element in row:
        elements.append(element.lower())

lines = int(file.readline().rstrip("\r\n"))

def recursive(word, index):
    if index >= len(word): return True
    p = []
    for element in elements:
        if word[index] == element[0]:
            if len(element) == 1:
                p.append(element)
            else:
                try:
                    if word[index + 1] == element[1]:
                        p.append(element)
                except IndexError:
                    continue
    if len(p) == 0: return False
    for possible in p:
        if recursive(word, index + len(possible)):
            return True
    return False

for i in range(lines):
    word = file.readline().rstrip("\r\n").lower()
    if recursive(word, 0):
        print "yes"
    else:
        print "no"
