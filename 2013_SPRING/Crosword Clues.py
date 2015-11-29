file = open("student_data/crosswordclues.dat")

words = []

for i in range(10):
    word = file.readline().strip("\r\n").split(" ")
    for w in word:
        words.append(w)

todo = []

while True:
    w = file.readline().rstrip("\r\n")
    if w == '': break
    todo.append(w)

for word in todo:
    p1 = []
    for w in words:
        if len(w) == len(word):
            p1.append(w)
    if len(p1) == 0:
        print "NO MATCH"
        continue

    p2 = []
    for w in p1:
        for i in range(len(w)):
            if not word[i] == '*' and not word[i] == w[i]:
                break
        else:
            p2.append(w)

    if len(p2) == 0:
        print "NO MATCH"
        continue
    else:
        s = ""
        for w in p2:
            s += w + " "
        print s
