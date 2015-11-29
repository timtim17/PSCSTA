file = open("student_data/knapsack.dat", "r")

lines = int(file.readline().strip("\r\n"))

def func(_list, result, max_weight):
    if len(_list) == 0:
        return result
    elif len(_list) == 1:
        w = 0
        for i in result:
            w += i['weight']
        w += _list[0]['weight']
        if w <= max_weight:
            return result + _list
        else:
            return result
    else:
        results = []
        for i in range(len(_list)):
            a = list(result)
            b = list(_list)
            a.append(b[i])
            del b[i]
            results.append(func(b, a, max_weight))
        good = []
        for result_index in range(len(results)):
            w = 0
            for i in results[result_index]:
                w += i['weight']
            if w <= max_weight:
                good.append(result_index)
        m = []
        for index in good:
            m.append(results[index])
        if m == []:
            return result
        ax = -1
        i = -1
        for o in range(len(m)):
            v = 0
            for p in m[o]:
                v += p['value']
            if v > ax:
                ax = v
                i = o
        return m[i]


for i in range(lines):
    max_weight = int(file.readline().strip("\r\n"))

    things = int(file.readline().strip("\r\n"))

    items = []

    for j in range(things):
        data = [int(x) for x in file.readline().strip("\r\n").split()]
        items.append({'value': data[0], 'weight': data[1], 'item': j + 1})

    print "knapsack capacity = %d" % max_weight

    p = []

    m = func(items, [], max_weight)

    total_weight = 0
    total_value = 0

    for item in m:
        total_weight += item['weight']
        total_value += item['value']

    print "total weight = %d" % total_weight
    print "total value = %d" % total_value
    for item in m:
        print "Item #%d - v=%d: w=%d" % (item['item'], item['value'], item['weight'])

    print
