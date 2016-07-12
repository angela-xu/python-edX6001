def f(s):
    return 'a' in s


def satisfiesF(L):
    '''
    Assumes L is a list of strings
    Assumes function f is defined that it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such that f(s) returns True, and no other elements
    
    returns the length of L after mutation
    '''
    l = [i for i in L if f(i) == True]
    L[:] = l
    return len(L)


L = ['a', 'b', 'a']
print satisfiesF(L)
print L
