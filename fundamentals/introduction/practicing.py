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

print(x.upper())
print(x.lower())
print(x.count('o'))
print(x.split())
print(x.split(None))
print(x.find('r'))
print(x.isalnum())
print(x.isalpha())
print(x.isdigit())
print(x.islower())
print(x.isupper())
#Why doesn't the above work?

# string.upper(): returns a copy of the string with all the characters in uppercase.
# string.lower(): returns a copy of the string with all the characters in lowercase.
# string.count(substring): returns number of occurrences of substring in string.
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# string.find(substring): returns the index of the start of the first occurrence of substring within string.
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# It is very important to remember the following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2
print(sum3)

# Exiting the function: Reaching a return statement always means "EXIT THIS FUNCTION NOW" whether or not there is more code. Any remaining code will not be run.

# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau

# Challenge 2:
#   Call the function again using your own name and print the results!

name2 = full_name("Robyn", "Lang")
print(name2)

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful() # output: good morning (repeated on 2 lines)
be_cheerful("tim") # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john") # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6) # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5) # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb") # output: good morning kb (repeated on 3 lines)

'''
no arguments are provided -- the defaults are used
one unnamed argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used
one named argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
both unnamed arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)
both named arguments provided -- values are assigned to associated parameter (and then order doesn't matter!)
'''

def multiply(num_list, num):
    print(num_list,  num)
    for x in range(len(num_list)):
        print(x)
        num_list[x] *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output: >>>[2,4,10,16]

# Challenge yourself!

person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
# Create a another person dictionary called person_2 and print it to the terminal
person_2 = {"first_name": "Robyn", "last_name": "Lang", "age": 44, "is_organ_donor": False}
print(person_2)

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
capitals["foo"] = "Huntsville"
capitals['bar'] = "Orlando"
# Add 2 key-value pairs to this dictionary.

# print the capitals dictionary to see how it changed!
print(capitals)

value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything



person = {
    "first": "Ada",
    "last": "Lovelace",
    "age": 42,
    "is_organ_donor": True
    }

# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"

# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)


if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")


countries_so_far = {
    "Mexico": 1,
    "Morocco": 1
    }
#dictionary

new_visits = [
    "Albania",
    "Mexico",
    "Togo",
    "Morocco"
    ]
#list

# To add Albania to the list
countries_so_far["Albania"] = 1
# To add 1 to the Mexico tally
countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
# your code here to finish updating your travel log!
countries_so_far["Togo"] = 1
countries_so_far["Morocco"] += 1

print(countries_so_far)


print(person["first_name"])
full_name = person["first_name"] + " " + person["last_name"]
# to access the values of a dictionary


my_dict = {
    "name": "Noelle",
    "language": "Python"
    }
for each_key in my_dict:
    print(each_key)
# output: name, language

for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python


capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"
    }

# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(resume_data["skills"][1]) # 'back-end' will print.
print(users[2]["first"]) # 'Eric' will print
