#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# 5 will be the result.


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# undefined/error will be the result, as arguments are required for the first function called, and none were supplied. Might be an error because the first function is not defined yet.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# the result will be 5, because once a function returns a value, it's over with.


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# the print statement will not work, because it is after the value is returned, and once a function is returned, it exits the function. So 5 will be printed.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# x will be undefined, as the called function has no return statement, only a print statement for debugging. Just kidding, I changed my mind...5 will be printed to the console.
# Oh, and turns out 'None' will be printed as well, since the function has no return value.


# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# I believe an error would be received, because this function has no return value.


# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# the result will be '25'


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# '100' will be printed to the console, and '10  will be returned when the function is called.


# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# '7' will be returned.
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# '14' will be returned.
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# '21' will be returned.


# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# '8' will be returned.


# #11
b = 500
print(b)
# '500' will be printed to the console.
def foobar():
    b = 300
    print(b)
print(b)
# '500' will be printed to the console.
foobar()
# '300' will be printed to the console.
print(b)
# '500' will be printed to the console.


# #12
b = 500
print(b)
# '500' will be printed to the console.
def foobar():
    b = 300
    print(b)
    return b
print(b)
# '500' will be printed to the console.
foobar()
# '300' will be printed to the console.
# '300' will be returned, but not stored anywhere.
print(b)
# '500' will be printed to the console.


# #13
b = 500
print(b)
# '500' will be printed to the console.
def foobar():
    b = 300
    print(b)
    return b
print(b)
# '500' will be printed to the console.
b=foobar()
# '300' will be printed to the console.
# '300' will be returned and stored in the b variable.
print(b)
# '300' will be printed to the console.


# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# '1' will be printed to the console.
# '3' will be printed to the console.
# '2' will be printed to the console.


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
# '1' will be printed to the console.
# '3' will be printed to the console.
# '5' will be printed to the console.
# '10' will be returned, but not stored anywhere.
# turns out none of this will happen...
print(y)
# '1' will be printed to the console.
# '3' will be printed to the console.
# '5' will be printed to the console.
# '10' will be printed to the console.
