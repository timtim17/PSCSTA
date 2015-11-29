file_elements = open("student_data/elements.dat", "r")

elements = []

for element in range(118):
    data = file_elements.readline().strip("\r\n").split(" - ")
    elements.append(data[1].lower())

file_cast = open("student_data/bad.dat", "r")

lines = int(file_cast.readline().strip("\r\n"))

for member in range(lines):
    data = file_cast.readline().strip("\r\n").split(" ")
    for name_index in range(len(data)):
        matches = []
        name = data[name_index]
        for char_index in range(len(name)):
            if name[char_index].lower() in elements:
                matches.append((name[char_index].lower(), char_index))
            try:
                if (name[char_index] + name[char_index + 1]).lower() in elements:
                    matches.append(((name[char_index] + name[char_index + 1]).lower(), char_index))
            except IndexError: pass
        matches.sort()
        if len(matches) == 0: continue
        element = matches[0]
        data[name_index] = name[:element[1]] + element[0].capitalize() + "_" + name[element[1] + (len(element[0])):]
    print " ".join(data)
