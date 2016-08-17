'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
'''

s = 'azcbobobegghakl'

total = 0
for i in s:
    if i in 'aeiou':
        total += 1
print('Number of vowels: ' + str(total))
