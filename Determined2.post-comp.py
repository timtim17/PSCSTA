file = open("data\\determined2.dat")
# file = open("D:\\JudgesData\\determined2.dat")

lines = int(file.readline().rstrip("\r\n"))

def find_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        returns = []
        for col in range(len(matrix)):
            m = []
            for row in range(1, len(matrix)):
                r = []
                for char in matrix[row][:col]:
                    r.append(char)
                for char in matrix[row][col + 1:]:
                    r.append(char)
                m.append(r)
            returns.append(find_determinant(m) * matrix[0][col])
        determinant = 0
        for i in range(len(returns)):
            if i % 2 == 0:
                determinant += returns[i]
            else:
                determinant -= returns[i]
        return determinant

for i in range(lines):
    matrix = []
    first_line = [int(x) for x in file.readline().rstrip("\r\n").split(" ")]
    matrix.append(first_line)
    for j in range(len(first_line) - 1):
        data = [int(x) for x in file.readline().rstrip("\r\n").split()]
        matrix.append(data)
    print find_determinant(matrix)
