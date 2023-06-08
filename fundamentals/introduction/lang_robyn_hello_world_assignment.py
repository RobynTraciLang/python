# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Robyn"
print('Hello', name + '!')	# with a comma
print('Hello ' + name + '!')	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 11
print('Hello', str(name) +'!')	# with a comma
print('Hello ' + str(name) + '!')	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." (I actually do!) with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print('I love to eat {} and {}.'.format(fave_food1, fave_food2)) # with .format()
print(f'I love to eat {fave_food1} and {fave_food2}.') # with an f string

name = "Robyn"
print(name.upper())
print(name.casefold())
print(name.islower())
print(name.lower())
print(name.split())
print(name.replace('R','b'))
print(name.partition('8'))
print(name.isalnum())
print(name.find('R'))