file = open("student_data/clockpaperscissors.dat", "r")

lines = int(file.readline().strip("\r\n"))

games = []

for i in range(lines):
    games.append([int(x) for x in file.readline().strip("\r\n").split(" ")])

for game in games:
    if game.count(0) >= 2:
        print "Player 2"
    else:
        print "Player 1"
