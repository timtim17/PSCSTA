file = open("student_data/invaders.dat", "r")

lines = int(file.readline().strip("\r\n"))

cities = []

for i in range(lines):
    t = file.readline().strip("\r\n").split(" : ")
    d = {
        'city': t[0],
        'distance': int(t[1]),
        'fallen': False
    }
    cities.append(d)
    del t

spread_rate = 1000
done = False
distance = 0
day = 0

while not done:
    day += 1
    distance += spread_rate
    print "Day %d" % day
    print "   Rate: %d Miles Per Day" % spread_rate
    for city in cities:
        if not city['fallen'] and city['distance'] <= distance:
            city['fallen'] = True
            if not spread_rate > 250000:
                spread_rate *= 2
            print "   %s has fallen!" % city['city']
    done = True
    for city in cities:
        if not city['fallen']:
            done = False
print "The aliens have taken over!"
