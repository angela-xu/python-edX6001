'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
'''

s = 'azcbobobegghakl'

sub = s[0]
temp = ''
for i in s[1:]:
    if i >= sub[-1]:
        sub += i
    else:
        if len(sub) > len(temp):
            temp = sub
            sub = i
        else:
            sub = i
if len(sub) > len(temp):
    temp = sub
print('Longest substring in alphabetical order is: ' + temp)
