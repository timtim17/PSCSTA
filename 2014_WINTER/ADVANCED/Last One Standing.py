file = open("student_data/lastonestanding.dat", "r")
lines = int(file.readline().strip("\r\n"))
games = []
for i in range(lines):
    tags = int(file.readline().strip("\r\n"))
    game = []
    for tag in range(tags):
        t = file.readline().strip("\r\n").split(" ")
        del t[1]
        game.append(t)
    games.append(game)
for game in games:
    people = {}
    for pair in game:
        for person in pair:
            people[person] = {
                "tagged": [],
                "frozen": False,
                "tagged_by": None
            }

    valid = True
    for pair in game:
        if people[pair[0]]['frozen'] or people[pair[1]]['frozen'] or pair[0] == pair[1]:
            valid = False
        else:
            people[pair[0]]['tagged'].append(pair[1])
            people[pair[1]]['frozen'] = True
            people[pair[1]]['tagged_by'] = pair[0]
            for person in people:
                if people[person]['tagged_by'] == pair[1]:
                    people[person]['frozen'] = False
    if valid:
        print "VALID GAME"
        for person in people:
            for key in people:
                if key not in people[person]['tagged'] and not key == person:
                    break
            else:
                print "Winner: %s" % person
                break
        else: print "Unfinished"
    else:
        print "INVALID GAME"
    print
