file = open("student_data/pacdude.dat", "r")

lines = int(file.readline())

good = ".X"

mazes = []

for i in range(lines):
    data = file.readline().strip("\r\n")
    width = 0
    height = 0
    s = ""
    for j in data:
        if j == " ":
            width = int(s)
            s = ""
        else:
            s += j
    height = int(s)

    rows = []
    for j in range(height):
        rows.append(file.readline().strip("\r\n"))

    mazes.append({
        'maze': rows,
        'stack': [],
        'completable': False
    })

for maze in mazes:
    complete = False
    came_from = 'left'
    pos = [1, 1]
    for row_index in range(len(maze['maze'])):
        for char_index in range(len(maze['maze'][row_index])):
            if maze['maze'][row_index][char_index] == "X":
                fruit_pos = [char_index, row_index]
    while not complete:
        if pos == fruit_pos:
            complete = True
            maze['completable'] = True
        movement = {
            'pos': list(pos),
            'movements': {
                'up': False,
                'down': False,
                'left': False,
                'right': False
            },
            'came_from': ""
        }
        if len(maze['stack']) > 0:
            l = maze['stack'][-1]['pos']
            if l[0] == pos[0]:
                if l[1] < pos[1]:
                    came_from = 'up'
                elif l[1] > pos[1]:
                    came_from = 'down'
            else:
                if l[0] < pos[0]:
                    came_from = 'left'
                elif l[0] > pos[0]:
                    came_from = 'right'
        else:
            came_from = None

        if maze['maze'][pos[1] - 1][pos[0]] in good:
            movement['movements']['up'] = None
        if maze['maze'][pos[1] + 1][pos[0]] in good:
            movement['movements']['down'] = None
        if maze['maze'][pos[1]][pos[0] - 1] in good:
            movement['movements']['left'] = None
        if maze['maze'][pos[1]][pos[0] + 1] in good:
            movement['movements']['right'] = None

        movement['came_from'] = came_from

        maze['stack'].append(movement)

        m = maze['stack'][-1]

        if m['came_from'] is not None:
            m['movements'][m['came_from']] = False

        if m['movements']['up'] is None:
            m['movements']['up'] = True
            pos[1] -= 1
        elif m['movements']['down'] is None:
            m['movements']['down'] = True
            pos[1] += 1
        elif m['movements']['left'] is None:
            m['movements']['left'] = True
            pos[0] -= 1
        elif m['movements']['right'] is None:
            m['movements']['right'] = True
            pos[0] += 1
        else:
            if len(maze['stack']) <= 0:
                complete = True
            else:
                pos = m['pos']
                if m['movements']['up']:
                    m['movements']['up'] = False
                elif m['movements']['down']:
                    m['movements']['down'] = False
                elif m['movements']['left']:
                    m['movements']['left'] = False
                elif m['movements']['right']:
                    m['movements']['right'] = False
                else:
                    complete = True

    if maze['completable']:
        print "NOM-NOM"
        for move in maze['stack']:
            maze['maze'][move['pos'][1]] = maze['maze'][move['pos'][1]][:move['pos'][0]] + " " + maze['maze'][move['pos'][1]][move['pos'][0] + 1:]
        maze['maze'][fruit_pos[1]] = maze['maze'][fruit_pos[1]][:fruit_pos[0]] + "O" + maze['maze'][fruit_pos[1]][fruit_pos[0] + 1:]
        for row in maze['maze']:
            print row
        print
    else:
        print "UH-OH!"
        print
