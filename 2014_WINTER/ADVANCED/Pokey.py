file = open("student_data/pokey.dat", "r")

lines = int(file.readline())

hands = []

for i in range(lines):
    data = file.readline().strip("\r\n")
    t = ""
    l = []
    def addToList(t):
        if t == "J":
            l.append(11)
        elif t == "Q":
            l.append(12)
        elif t == "K":
            l.append(13)
        elif t == "A":
            l.append(14)
        else:
            l.append(int(t))
    for j in data:
        if j == " ":
            addToList(t)
            t = ""
        else:
            t += j
    addToList(t)
    del t
    l.sort()
    hands.append(l)
    del l

for hand in hands:
    y = False
    if (hand.count(hand[0]) == 3 and hand.count(hand[-1]) == 2) or (hand.count(hand[0]) == 2 and hand.count(hand[-1]) == 3):
        print "FULL HOUSE"
        y = True
    elif hand[1] == hand[0] + 1 and hand[2] == hand[0] + 2 and hand[3] == hand[0] + 3 and hand[4] == hand[0] + 4:
        print "STRAIGHT"
        y = True
    else:
        for i in hand:
            if hand.count(i) >= 3:
                print "TRIPLE"
                y = True
                break
            elif hand.count(i) >= 2:
                print "PAIR"
                y = True
                break
        if not y:
            print "ZILCH"
