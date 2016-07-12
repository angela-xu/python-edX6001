def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an int
    '''
    re = []
    for i in aDict.keys():
        if aDict[i] == target:
            re.append(i)
    re.sort()
    return re
