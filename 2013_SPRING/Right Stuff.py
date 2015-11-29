file = open("student_data/rightstuff.dat")

lines = int(file.readline().rstrip("\r\n"))

for i in range(lines):
    data = [float(x) for x in file.readline().rstrip("\r\n").split(" ")]
    ans = data[0]
    del data[0]
    a = sum(data)/len(data)

    # Accuracy
    z = a - ans
    x = z/ans
    c = x * 100
    del z, x
    accurate = abs(c) <= 5

    # Precision
    r = max(data) - min(data)
    precise = r <= (a * .1)

    if accurate and precise:
        print "Both"
    elif accurate:
        print "Accurate"
    elif precise:
        print "Precise"
    else:
        print "Neither"
