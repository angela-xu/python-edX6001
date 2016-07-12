'''
A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes").
Here are some examples: nametag / gateman, dog / god, live / evil, desserts / stressed
Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.
'''

def semordnilapWrapper(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return False
    if len(str1) == 1 or len(str1) == 1:
        return False
    if str1 == str2:
        return False
    if len(str1) != len(str2):
        return False
    
    def semordnilap(str1, str2):
        if len(str1) == 1:
            return str1 == str2
        return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])
    
    return semordnilap(str1, str2)

print(semordnilapWrapper('', 'abc'))
print(semordnilapWrapper('', ''))
print(semordnilapWrapper('ab', ''))
print(semordnilapWrapper('a', 'c'))
print(semordnilapWrapper('abba', 'abba'))
print(semordnilapWrapper('word', 'ord'))
print(semordnilapWrapper('nametag', 'gateman'))
print(semordnilapWrapper('live', 'evil'))

print('\n')
print('Correct Output: False, False, False, False, False, False, True, True')
