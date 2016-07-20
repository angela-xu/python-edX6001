#
# #1: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == '':
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]


#
# test case of #1
#
print('--------------- Test results of #1 ---------------')
print('')

import random
import string
import time
s = ''
n = 10
for i in range(n):
    s += string.ascii_lowercase[random.randint(0, 25)]

print('Original string is ' + '\n' + s)
print('')

start_time = time.time()
a = reverseString(s)
print("--- %s seconds ---" % (time.time() - start_time))
print('Reversed string is ' + '\n' + a)
print('')

start_time = time.time()
b = s[::-1]
print("--- %s seconds ---" % (time.time() - start_time))
print('Reversed string is ' + '\n' + b)
print('\n')



#
# #2: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == '':
        return True
    else:
        return x[0] in word and x_ian(x[1:], word[word.index(x[0]) + 1 :])


#
# test case of #2
#
print('--------------- Test results of #2 ---------------')
print('')

print(str(x_ian('abcd', 'ab')) + ' --- should be False')
print(str(x_ian('eric', 'meritocracy')) + ' --- should be True')
print(str(x_ian('eric', 'cerium')) + ' --- should be False')
print(str(x_ian('john', 'mahjong')) + ' --- should be False')
print('\n')



#
# #3: Typewriter
#
def insertNewlinesRec(text, lineLength):
    if text=='':
        return ''
    elif lineLength==1:
        return text
    else:
        return insertNewlinesRec(text[1:], lineLength-1)


def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.
    
    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping the next word.

    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) < lineLength:
        return text
    b= insertNewlinesRec(text, lineLength)
    a= b.split(' ')
    if b[0] == ' ':
        return text[:lineLength - 1]+ '\n'+ insertNewlines (text[(lineLength):], lineLength)
    else:
        c= len(a[0])
        return text[:(c+ lineLength)]+ '\n'+ insertNewlines (text[(c + lineLength):], lineLength)


#
# test case of #3
#       
print('--------------- Test results of #3 ---------------')
print('')

o_str = "That was a really nice day. My dog Alee did enjoy a wonderful time at the Green Lake's Park."
linelen = 26
n_str = insertNewlines(o_str, linelen)
print('Original Text: ' + o_str)
print('')
print('New Text: ' + '\n' + n_str)

