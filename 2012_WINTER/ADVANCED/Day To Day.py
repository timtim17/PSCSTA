file = open("student_data/daytoday.dat", "r")

lines = int(file.readline().rstrip("\r\n"))

month_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

for i in range(lines):
    data = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    first_date = data[:3]
    second_date = data[3:]
    del data
    a = first_date
    days = 0
    while not a == second_date:
        a[1] += 1
        days += 1
        if a[1] > month_days[a[0]]:
            if a[0] == 2 and a[2] % 4 == 0 and a[1] == 29:
                continue
            a[1] = 1
            a[0] += 1
        if a[0] > 12:
            a[0] = 1
            a[2] += 1
    days -= 1
    print days

