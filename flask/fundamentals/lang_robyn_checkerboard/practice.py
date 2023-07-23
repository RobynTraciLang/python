# create a function that, given an input string, returns a boolean whether parentheses in that string are valid, Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n0)(t(0)k", return false.

# def valid_parentheses(input_string):
#     open_count = 0
#     closed_count = 0
#     for i in input_string:
#         if i == ")":
#             closed_count += 1
#         if i == "(":
#             open_count += 1
#         if open_count == closed_count:
#             print(open_count)
#             print(closed_count)
#             print(True)
#             return True


# valid_parentheses("y(3(p)p(3)r)s")
# valid_parentheses("n(0(p)3")
# valid_parentheses("n0)(t(0)k")

# def are_parentheses_valid(input_string):
#     stack = []
#     opening_parentheses = set("([{")
#     closing_parentheses = set(")]}")

#     for char in input_string:
#         if char in opening_parentheses:
#             stack.append(char)
#         elif char in closing_parentheses:
#             if not stack or not is_matching_pair(stack[-1], char):
#                 return False
#             stack.pop()

#     return len(stack) == 0

# def is_matching_pair(opening, closing):
#     pairs = {
#         '(': ')',
#         '[': ']',
#         '{': '}',
#     }
#     return pairs[opening] == closing

# # Test cases
# print(are_parentheses_valid("y(3(p)p(3)r)s"))  # Output: True
# print(are_parentheses_valid("n(0(p)3"))       # Output: False
# print(are_parentheses_valid("n0)(t(0)k"))     # Output: False

def are_parentheses_valid(input_string):
    stack = []
    # opening_parentheses = "([{"
    # closing_parentheses = ")]"

    for i in input_string:
        if i == "(":
            stack.append(i)
            print(stack)
        if i == ")":
            if not stack:
                return False

# Test cases
print(are_parentheses_valid("y(3(p)p(3)r)s"))  # Output: True
print(are_parentheses_valid("n(0(p)3"))       # Output: False
print(are_parentheses_valid("n0)(t(0)k"))     # Output: False
