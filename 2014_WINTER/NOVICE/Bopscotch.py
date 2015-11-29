file = open("student_data/bopscotch.dat", "r")

lines = int(file.readline().strip("\r\n"))

for i in range(lines):
    end = int(file.readline().strip("\r\n"))
    print "/ %d \\" % end
    if end == 2:
        pass
    elif end % 2 == 0:
        print " [%d] " % (end - 1)
        print " [%d] " % (end - 2)
        for num in range(end - 2, 3, -3):
            print "[%d][%d]" % (num - 2, num - 1)
            print " [%d] " % (num - 3)
    elif end % 3 == 0:
        print " [%d] " % (end - 1)
        for num in range(end - 1, 3, -3):
            print "[%d][%d]" % (num - 2, num - 1)
            print " [%d] " % (num - 3)
    else:
        for num in range(end - 1, 1, -3):
            print "[%d][%d]" % (num - 1, num)
            print " [%d] " % (num - 2)
    print "\ 1 /"
    print
