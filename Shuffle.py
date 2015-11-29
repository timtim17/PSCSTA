# file = open("data\\shuffle.dat")
file = open("D:\\JudgesData\\shuffle.dat")

strings = []

while True:
    data = file.readline().rstrip("\r\n")
    if data == '': break
    strings.append(data)

for string in strings:
    words = []
    string = string.split(" ")
    for word in string:
        if word not in words:
            words.append(word)
    words.sort()
    print " ".join(words)