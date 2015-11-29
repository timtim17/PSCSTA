names = ["Austin", "Daniel"]
length = reduce(lambda x, y: len(x) + len(y), names)

print "Hello Great and Grand Judges! We are %s and %s. We go to Eastlake, where every day we have %d letters in our names combined. Have a wolf strong day!" % (names[0], names[1], length)
