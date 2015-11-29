path = "data\\"
# path = "D:\\JudgesData\\"

files = ['accounting.dat', 'bank.dat', 'buoyancy.dat', 'cross.dat', 'cursed.dat', 'determined1.dat', 'determined2.dat', 'drought.dat', 'histonum.dat', 'shuffle.dat', 'sineup.dat', 'splatter.dat']

length = 0

for file in files:
    file = open(path + file)
    length += len(file.readlines())

print "THERE ARE %d LINES OF DATA FOR THIS PACKET" % length
