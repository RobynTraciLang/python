# - create a function that, given an input string, returns a boolean whether parenteses in that string are valid. given input "y(3(p)p(3)r)s", returns true.
#     given "n(0(p)3", return false. given "n)0(t(0)k", return false

def valid_parenthesis(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print(valid_parenthesis("y(3(p)p(3)r)s"))
print(valid_parenthesis("n(0(p)3"))
print(valid_parenthesis("n)0(t(0)k"))


# def valid_parentheses(string):
#     open_count = 0
#     closed_count = 0
#     for i in string:
#         if i == "(":
#             open_count += 1
#         if i == "))":
#             closed_count


# def valid_parenthesis(string):
#     stack = []
#     for char in string:
#         if char == '(':
#             stack.append(char)
#         elif char == ')':
#             if not stack:
#                 return False
#             stack.pop()
#     return not stack

# print(valid_parenthesis("y(3(p)p(3)r)s"))
# print(valid_parenthesis("n0(t(0k"))

def wednesday(string):
    open_par = []
    closed_par = []
    for i in string:
        if len(closed_par) > len(open_par):
            return False
        else:
            if i == "(":
                open_par.append(i)
            elif i == ")":
                closed_par.append(i)
            else: continue
    if len(closed_par) == len(open_par):
        return True

print(wednesday("y(3(p)p(3)r)s"))