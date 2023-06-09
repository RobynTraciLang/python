'''
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
'''

# Basic
for i in range(151):
    print(i)

# Multiples of Five
for i in range(5, 1001, 5):
    print(i)

# Counting, the Dojo Way
for i in range(1,101):
    if i % 2 == 0 and i % 5 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# Whoa. That Sucker's Huge
odds_sum = 0
for i in range(1, 500001, 2):
    odds_sum += i
print(odds_sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Flexible Counter
low_num = 3
high_num = 111
mult = 5
for i in range(low_num, high_num):
    if i % mult == 0:
        print(i)