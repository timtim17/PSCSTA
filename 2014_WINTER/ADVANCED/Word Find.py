file = open("student_data/wordfind.dat", "r")

lines = int(file.readline())

words = []

for i in range(lines):
    data = file.readline().strip("\r\n")
    words.append(data)

rows = []
for i in range(10):
    rows.append(file.readline().replace(" ", ""))

matches = []

for word in words:
    for row_index in range(len(rows)):
        row = rows[row_index]
        for letter_index in range(len(row)):
            if row[letter_index] == word[0]:
                try:
                    good = True
                    for i in range(len(word)):
                        if not row[letter_index + i] == word[i]:
                            good = False
                    if good:
                        matches.append((letter_index, row_index))
                except IndexError: pass

columns = []
for i in range(10):
    s = ""
    for row in rows:
        s += row[i]
    columns.append(s)

for word in words:
    for column_index in range(len(columns)):
        column = columns[column_index]
        for letter_index in range(len(column)):
            if column[letter_index] == word[0]:
                try:
                    good = True
                    for i in range(len(word)):
                        if not column[letter_index + i] == word[i]:
                            good = False
                    if good:
                        matches.append((column_index, letter_index))
                except IndexError: pass

for match in matches:
    print "%d %d" % match
