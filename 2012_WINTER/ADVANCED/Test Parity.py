file = open("student_data/testparity.dat", "r")

scores = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]

for score in range(len(scores)):
    if 0 < scores[score] <= 25:
        scores[score] *= 2
    elif 25 < scores[score] <= 50:
        scores[score] += scores[score] * 0.5
    elif 50 < scores[score] <= 75:
        scores[score] += scores[score] * 0.25
    elif 75 < scores[score] < 100:
        continue
    elif 100 < scores[score] < 120:
        scores[score] -= scores[score] * 0.1

print " ".join([str(int(x)) for x in scores])
