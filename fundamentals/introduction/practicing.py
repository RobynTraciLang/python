print(type(24))
print(type(3.9))
print(type(3j))

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))


import random
print(random.randint(2,5)) # provides a random number between 2 and 5

import random
print(random.randint(2,5))

import random
print(random.randint(2,5))

print("this is a sample string")

name = "Zen"
print("My name is", name)

name = 'Zen'
print('My name is', name)

name = "Zen"
print("My name is " + name)

name = 'Zen'
print('My name is ' + name)

name = 7
print('My name is', name)

# name = 7
# print('My name is ' + name) #error message triggered

name = 7
print('My name is ' + str(name))

# total = total + user_val		# output: TypeError
total = 35
user_val = "26"
total = total + int(user_val)		# total will be 61
print(total)

first_name = "Robyn Traci"
last_name = "Lang"
age = 44
print(f"My name is {first_name} {last_name} and I am {age} years old.")

first_name = 'Zen'
last_name = 'Coder'
age = 27
print(f'My name is {first_name} {last_name} and I am {age} years old.')

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.
print('My name is {} {} and I am {} years old.'.format(first_name, last_name, age))

# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = (f"Hello my name is {first_name} {last_name}")

print(greeting) 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

print(f"I started in the field when I was {age - years_experience} years old.")
# Desired output: I started in the field when I was 31 years old.



hw = "Hello %s" % "world," 	# with literal values
py = "I love Python %d!" % 3
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d." % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world"
print(x.title())
# # output:
# "Hello World"

# print(x.upper)
# print(x.lower)
# print(x.count())
# print(x.split())
# print(x.split(3))
# print(x.find())
# print(x.isalnum())
# print(x.isalpha())
# print(x.isdigit())
# print(x.islower())
# print(x.isupper())
#Why doesn't the above work?

# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
