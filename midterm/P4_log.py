def myLog(x, b):
    '''
    x: a positive int
    b: a positive int; b >= 2
    
    returns: the largest power of b such that b to that power is still
             less than or equal to x.
    '''
    a = 0
    while b ** a < x:
           a += 1
    if b ** a == x:
        return a
    else:
        return a - 1

print(myLog(1, 2)), ('should be 0')
print(myLog(2, 2)), ('should be 1')
print(myLog(16, 2)), ('should be 4')
print(myLog(15, 3)), ('should be 2')
