# import math

# def how_many_of_each_coin(cents):

#     quarters = 0
#     dimes = 0
#     nickels = 0
#     pennies = 0

#     if math.floor(cents/25) >=1:
#         quarters = math.floor(cents/25)
#         cents -= quarters * 25
#     if math.floor(cents/10) >=1:
#         dimes = math.floor(cents/10)
#         cents -= dimes * 10
#     if math.floor(cents/5) >=1:
#         nickels = math.floor(cents/5)
#         cents -= nickels * 5
#     if math.floor(cents/1) >=1:
#         pennies = math.floor(cents/1)
#         cents -= pennies * 1

#     return quarters, dimes, nickels, pennies

# print(how_many_of_each_coin(84))
# print(how_many_of_each_coin(250))
# print(how_many_of_each_coin(12))
# print(how_many_of_each_coin(8000))


# create a function that given a string, returns the integer made from the string's digits. Given "0s1a3y5w7h9a2t4", the function should return the number 1357924

# def return_integer_from_digits(string):
#     integer_from_digits = 0
#     for digit in string:
#         if digit = int()
#         if digit > 1 and digit < 9:
#             integer_from_digits += digit

#     print(integer_from_digits)
#     return integer_from_digits

# def letters_numbers(input):
#     output = ''
#     first = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#     for i in input:
#         if i in first:
#             output += i
#     return int(output)

# print(letters_numbers("0s1a3y5w7h9a2t4"))

# # return_integer_from_digits("0s1a3y5w7h9a2t4")

# def get_digits(string):
#     just_digits = ""
#     for i in string:
#         if i.isdigit():
#             just_digits += i
#     return int(just_digits)

# print(get_digits("0s1a3y5w7h9a2t4"))

# - create function clockHandAngles(seconds) that, given the number of seconds since 12:00:00, will print the angles ( in degress ) of the hour, minute and second hands. As a quick review, there are 360 degrees in a full arc rotation. Treat "stright-up" 12:00:00 as 0 degress for all hands

# create a function sum_to_one(num) that, given a number, will repeatedly sum the digits until the new number is only one digit long. Return that finalonedigitnumber.

# def sum_to_one(num):
#     sum = 0
#     final_one_digit_num = 0
#     num_as_string = str(num)
#     for i in num_as_string:
#         sum += int(i)
#         print(sum)
#         num = sum
#         num_as_string = str(num)
#     final_one_digit_num = sum

# sum_to_one(5789)

print(5789 % 10)
print(5789/10)
print(5789//=10)
print(578 % 10)
print(578/10)
print(29%10)
print(29/10)