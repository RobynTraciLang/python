# 1. TASK: print "Hello World"
print( your code here )
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print( your code here )	# with a comma
print( your code here )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print( your code here )	# with a comma
print( your code here )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( your code here ) # with .format()
print( your code here ) # with an f string

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']

# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

some_nums = [44,56,2,3,12,19,6]
print("Get started by writing your own code!")

# Some optional challenges to assess and refine your understanding:

# Print the length of the list.
print(len(some_nums))

# Use another python built-in function and print the result.
print(max(some_nums))
print(min(some_nums))

# Remove an item from the list. Remember to verify that it was removed.
some_nums.pop()
print(some_nums)

# Utilize a method from the documentation and print the result.
some_nums.reverse()
print(some_nums)

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
        print("bigger than 50")
else:
    print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
    # nothing happens, because the statement is false

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.
for x in range(1, 21):
    print(x)

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz

# OR

for v in my_list:
    print(v)
# output: abc, 123, xyz

countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0, len(countries)):
    print("Index:", integer)
    # Challenge 2: print the index here
    print("Country:", countries[integer])
    # Challenge 3: print the country here

# Looping over values only...
for country in countries:
    print("Country: " + country)
    # Challenge 4: print the country here

for count in range(0,5):
    print("looping =", count)

# can rewrite as the while loop below...

count = 0
while count < 5:
    print("looping - ", count)
    count += 1


# basic syntax for a while loop in python.
#while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

y = 3
while y > 0:
    print(y)
    y -= 1
else:
    print("Final else statement")

"""
Loop Control
We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

When you want finer control over your loops, use the following statements to do so.

Break
The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

When loops are nested, a break will only exit from the innermost loop.
"""

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

'''
Notice that when the loop got to the letter "i", we stopped looping.

Continue
The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
'''
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

