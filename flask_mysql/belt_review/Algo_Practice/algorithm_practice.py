# A Narcissistic Number is a positive number which is the sum of
# its own digits, each raised to the power of the number of digits
# in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# def is_narcissistic_number(number):
#     if number < 0:
#         print("not a narcissistic number.")
#         return False
#     elif number > 0:
#         digits = []
#         for digit in str(number):
#             digits.append(digit)
#         print(digits)
#         narc_number = 0
#         for character in digits:
#             current_number = int(character) ** len(digits)
#             print(current_number)
#             narc_number += current_number
#         if narc_number == number:
#             print('This number is narcissistic!')
#             return True
#         if narc_number != number:
#             print('This number is NOT narcissistic.')
#             return False


# is_narcissistic_number(153)

# is_narcissistic_number(3749)

# - median of sorted arrays
#         given two arrays that are sorted but not necessarily the same length, find the median value. for example, if given ([1,5,9], [1,2,3,4,5,6]), return 4. if the number of values is even reutrn the average of the two middle values. if given ([1,5,9], ([1,2,3,4,5])), return 3.5.
#         second: expand your function to accept three arrays instead of two
#         third: rework your function to correctly handle an arbitray number of arrays

# For a small data set, you first count the number of data points (n) and arrange the data points in increasing order. If the number of data points is uneven, you add 1 to the number of points and divide the results by 2 to get the rank of the data point whose value is the median. The rank is the position of the data point after the data set has been arranged in increasing order: the smallest value is rank 1, the second-smallest value is rank 2, etc.

# There are n = 7 data points, which is an uneven number. The median will be the value of the data points of rank

# (n + 1) ÷ 2 = (7 + 1)  ÷ 2 = 4.

# There are now n = 8 data points, an even number. The median is the mean between the data point of rank

# n ÷ 2 = 8 ÷ 2 = 4

# and the data point of rank

# (n ÷ 2) + 1 = (8 ÷ 2) +1 = 5

# Therefore, the median time is (25.2 + 25.6) ÷ 2 = 25.4 seconds.

def find_median_of_sorted_arrays(list1, list2):
    combined_list