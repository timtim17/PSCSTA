from math import ceil

file = open("student_data/vowely.dat")

lines = int(file.readline().rstrip("\r\n"))

vowels = "aeiou"

for i in range(lines):
    word = file.readline().rstrip("\r\n").lower()
    v = 0
    for c in word:
        if c in vowels:
            v += 1
    if v >= ceil(float(len(word))/2):
        print "YES"
    else:
        print "NO"
