# file = open("data\\cross.dat")
file = open("D:\\JudgesData\\cross.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    words =  file.readline().rstrip("\r\n").split(" ")
    del words[1]
    a = False
    p = None
    c = 0
    while c < len(words[0]) and p is None:
        for char1 in range(len(words[1])):
            if words[0][c] == words[1][char1]:
                a = True
                p = (c, char1)
        c += 1
    if not a:
        print "none"
    else:
        for c in range(len(words[1])):
            if c == p[1]:
                print words[0]
            else:
                print (" " * p[0]) + words[1][c]
    print
