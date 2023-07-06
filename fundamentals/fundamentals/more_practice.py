# Threes and Fives
#         Write a function threesFives() that adds each value from 100 to 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both.
#         display the final sum in the console

def threes_fives():
    sum = 0
    for i in range(100, 4000001):
        if i % 3 == 0 and i % 5 != 0:
            sum += i
        elif i % 3 != 0 and i % 5 == 0:
            sum += i
    print(sum)
    return sum

threes_fives()

#     Sum to One Digit
#         Write a function sumToOne(num) that given a number sums that number's digits repeatedly until the sum is only one digit. return that final one digit results.
#         sumToOne(18) would return 9

def sum_to_one(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num

result = sum_to_one(18)
print(result)  # Output: 9

# to include positive and negative integers:
def sum_to_one(num):
    num = abs(num)  # Take the absolute value of the number

    while num > 9:
        num = sum(int(digit) for digit in str(num))

    return num

result = sum_to_one(-18)
print(result)  # Output: 9


# our attempt during class:
def sum_to_one(num):
    while sum > 9:
        num = sum()


        return result

sum_to_one(18)