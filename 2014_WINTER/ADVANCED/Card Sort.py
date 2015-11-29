from sys import stdout

file = open("student_data/cardsort.dat", "r")

lines = int(file.readline().strip("\r\n"))

decks = []

def convert(card, to_num):
    if to_num:
        if card == "J":
            return 11
        elif card == "Q":
            return 12
        elif card == "K":
            return 13
        elif card == "A":
            return 1
        else:
            return int(card)
    else:
        if card == 11:
            return "J"
        elif card == 12:
            return "Q"
        elif card == 13:
            return "K"
        elif card == 1:
            return "A"
        else:
            return str(card)

for i in range(lines):
    l = [x.split(" ") for x in file.readline().strip("\r\n").split(", ")]
    for i in l:
        i[1] = convert(i[1], True)
    decks.append(l)

for deck in decks:
    deck = sorted(deck)
    for card in deck:
        stdout.write("%s %s, " % (card[0], convert(card[1], False)))
    stdout.write("\n")
