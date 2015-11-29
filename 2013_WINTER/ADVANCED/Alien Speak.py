file = open("student_data/alienspeak.dat", "r")

lines = int(file.readline().strip("\r\n"))

def recursive(listA, indexA, listB, indexB):
    if indexA >= len(listA) or indexB >= len(listB): return 0
    temp = 0
    for i in range(indexA, len(listA)):
        k = i
        try:
            j = listB[indexB:].index(listA[k])
            j += indexB
        except:
            continue
        temp = max(temp, 1 + recursive(listA, k + 1, listB, j + 1))
    return temp

for i in range(lines):
    data = [list(x) for x in file.readline().strip("\r\n").split(" ")]
    # matches = []
    #
    # for c in range(len(data[0])):
    #     a = 0
    #     m = []
    #     for char in range(c, len(data[0])):
    #         for j in range(a, len(data[1])):
    #             if data[0][char] == data[1][j]:
    #                 m.append(data[0][char])
    #                 a = j + 1
    #                 break
    #     matches.append(len(m))
    #
    # print matches
    print recursive(data[0], 0, data[1], 0)
