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

