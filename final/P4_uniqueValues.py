def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if nont
    '''
    if aDict == {}:
        return []
    elif len(aDict.keys()) == 1:
        return aDict.keys()

    l = []
    a = []
    for i in aDict.keys():
        for j in aDict.keys():
            if aDict[i] == aDict[j] and i != j:
                a.append(i)
                a.append(j)
    for i in aDict.keys():
        if i not in a:
            l.append(i)
    l.sort()
    return l


a = {}
b = {1:2}
c = {1:1, 3:2, 6:0, 7:0, 8:4, 10:0}
d = {1:1, 2:1, 3:1}


for i in [a, b, c, d]:
    print(uniqueValues(i))
    print('')
