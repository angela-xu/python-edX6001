'''
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s
'''

s = 'azcbobobegghakl'

total = 0
for i in range(len(s)-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        total += 1
print('Number of times bob occurs is: ' + str(total))
