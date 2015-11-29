# file = open("data\\drought.dat")
file = open("D:\\JudgesData\\drought.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    weather = [float(x) for x in file.readline().rstrip("\r\n").split(" ")]
    ave = weather[0]
    del weather[0]
    y1 = sum(weather[:12])
    y2 = sum(weather[12:])
    if y1 >= ave * 2 and y2 >= ave * 2:
        print "drought over"
    elif y1 >= ave and y2 >= ave:
        print "improving"
    else:
        print "continuing"