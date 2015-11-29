file = open("student_data/gamereviews.dat", "r")

lines = int(file.readline().strip("\r\n"))

reviews = []

for i in range(lines):
    l = file.readline().strip("\r\n").split(", ")
    del l[0]
    reviews.append(l)

games = {}

for review in reviews:
    if review[0] in games:
        games[review[0]]['rating'] += float(review[1])
        games[review[0]]['total'] += 1
    else:
        games[review[0]] = {
            'rating': 0.0,
            'total': 0
        }
        games[review[0]]['rating'] = float(review[1])
        games[review[0]]['total'] = 1

for game in games:
    games[game]['rating'] /= games[game]['total']
    print "%s gets %.1f stars." % (game, games[game]['rating'])
