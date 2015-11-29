from math import sin
from math import radians

# file = open("data\\sineup.dat")
file = open("D:\\JudgesData\\sineup.dat")

numbers = []

while True:
    data = file.readline().rstrip("\r\n")
    if data == '': break
    numbers.append([int(x) for x in data.split(" ")])

for number in numbers:
    D = number[0]
    A = number[1]
    B = number[2]
    C = 180 - A - B
    print "Circumcircle diameter = %d" % D
    print "Angles are %d, %d, and %d" % (A, B, C)
    print "Corresponding sides are %d, %d and %d" % (round(D * sin(radians(A)), 0), round(D * sin(radians(B)), 0), round(D * sin(radians(C)), 0))
