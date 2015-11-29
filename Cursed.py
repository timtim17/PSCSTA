# file = open("data\\cursed.dat")
file = open("D:\\JudgesData\\cursed.dat")

months = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}

while True:
    data = file.readline().rstrip("\r\n")
    if data == '': break
    data = data.split(" ")
    data[0] = months[data[0]]
    data[1] = data[1][:len(data[1]) - 1]
    date = '%s%02d%04d' % (data[0], int(data[1]), int(data[2]))
    if date == date[::-1]:
        print date + ": DON'T TRAVEL"
    else:
        print date + ": OK TO TRAVEL"
