num1 = 42 #variable declaration, number data type
num2 = 2.3 #variable declaration, number data type
boolean = True #variable declaration, boolean data type
string = 'Hello World' #variable declaration, string data type, sequence
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, string data type, list, initialize list, sequence
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, number data type, string data type, boolean data type, dictionary, initialize dictionary, sequence
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, string data type, tuple, initialize tuple, sequence
print(type(fruit)) #log statement, type check, access tuple value
print(pizza_toppings[1]) #log statement, access list value
pizza_toppings.append('Mushrooms') #add list value, function return
print(person['name']) #log statement, access dictionary value
person['name'] = 'George' #change dictionary value, delete dictionary value
person['eye_color'] = 'blue' #add dictionary value
print(fruit[2]) #log statement, access tuple value

if num1 > 45: #if conditional
    print("It's greater") #log statement
else: #else conditional
    print("It's lower") #log statement

if len(string) < 5: #length check, if conditional
    print("It's a short word!") #log statement
elif len(string) > 15: #length check, elif conditional
    print("It's a long word!") #log statement
else: #else conditional
    print("Just right!") #log statement

for x in range(5): #for loop start, for loop increment, for loop sequence
    print(x) #log statement, for loop stop
for x in range(2,5): #for loop start, for loop increment, for loop sequence
    print(x) #log statement, for loop stop
for x in range(2,10,3): #for loop start, for loop increment, for loop sequence
    print(x) #log statement, for loop stop
x = 0
while(x < 5): #while loop start
    print(x) #log statement, while loop stop
    x += 1 #while loop increment

pizza_toppings.pop() #delete list value, function return
pizza_toppings.pop(1) #delete list value, function return

print(person) #log statement
person.pop('eye_color') #delete dictionary value, function return
print(person) #log statement

for topping in pizza_toppings: #for loop start, for loop sequence
    if topping == 'Pepperoni': #if conditional
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if conditional
        break #for loop break, for loop return?

def print_hello_ten_times(): #function
    for num in range(10): #for loop start, for loop increment, for loop sequence
        print('Hello') #log statement

print_hello_ten_times() #function

def print_hello_x_times(x): #function, function parameter
    for num in range(x): #for loop start, for loop increment, for loop sequence (list, tuple, or range?)
        print('Hello') #log statement

print_hello_x_times(4) #function, function argument

def print_hello_x_or_ten_times(x = 10): #function, function parameter
    for num in range(x): #for loop start, for loop increment, for loop sequence
        print('Hello') #log statement, for loop stop

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #functin, function argument


"""
Bonus section
"""
#multiline comment

"""
print(num3) #log statement, single-line comment
num3 = 72 #variable declaration, single-line comment, number data type
fruit[0] = 'cranberry' #single-line comment, change tuple value, delete tuple value
print(person['favorite_team']) #log statement, single-line comment, KeyError: 'favorite_team'
print(pizza_toppings[7]) #log statement, single-line comment, IndexError: list index out of range
  print(boolean) #log statement, single-line comment, IndentationError: unexpected indent
fruit.append('raspberry') #single-line comment, AttributeError: 'tuple' object has no attribute 'append', function return
fruit.pop(1) #single-line comment, AttributeError: 'tuple' object has no attribute 'pop', function return
""" #multi-line comment