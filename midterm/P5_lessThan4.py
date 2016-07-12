def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    l = []
    for i in aList:
        if len(i) < 4:
            l.append(i)
    return l
