# My solution
def valid_parentheses(str):
    parentheses = []
    for ch in str:
        # case 1 closing without opening
        if ch == ')' and not parentheses:
            return False
        # case 2 closing and opening
        if ch == ')':
            parentheses.pop()
        # case 3 opening
        elif ch == '(':
            parentheses.append(ch)
    return not parentheses


# Other solution
# def valid_parentheses(str):
#     counter = 0
#     for ch in str:
#         if ch == '(':
#             counter += 1
#         if ch == ')':
#             counter -= 1
#         if counter < 0:
#             return False#
#     return True if counter == 0 else False


print(valid_parentheses("  ("))  # False
print(valid_parentheses(")test"))  # False
print(valid_parentheses(""))  # True
print(valid_parentheses("hi())("))  # False
print(valid_parentheses("hi(hi)()"))  # True
