from math import ceil

file = open("student_data/taxi.dat", "r")

one_fifth = 1/5.0

lines = int(file.readline().rstrip("\r\n"))

def calculate_mileage_cost(ride):
    distance = ride[0]
    if distance <= one_fifth:
        return 0.50
    else:
        return 0.50 + (0.22 * ceil((distance - one_fifth)/one_fifth))

for i in range(lines):
    data = [float(x) for x in file.readline().rstrip("\r\n").split(" ")]
    print "$%.2f" % (calculate_mileage_cost(data) + (0.20 * ceil(data[1]/60)))
