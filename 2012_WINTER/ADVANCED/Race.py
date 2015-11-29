file = open("student_data/gender_race.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

racers = []
male = []
female = []

for i in range(lines):
    data = file.readline().rstrip("\r\n").split(" ")
    data[1] = int(data[1])
    racer = (data[1], data[0], data[2])
    racers.append(racer)
    if data[2] == 'M':
        male.append(racer)
    else:
        female.append(racer)

racers.sort()
male.sort()
female.sort()

def print_racer(racer):
    print "%s %d %s" % (racer[1], racer[0], racer[2])

print_racer(racers[0])
print_racer(racers[1])

print_racer(female[0])
print_racer(female[1])

print_racer(male[0])
print_racer(male[1])
