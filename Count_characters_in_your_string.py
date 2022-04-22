# def count(string):
#     result = {}
#     for char in string:
#         if char not in result:
#             result[char] = 1
#         else:
#             result[char] += 1
#     return result
#

def count(string):
    return {i: string.count(i) for i in string}

print(count('aba'))
print(count(''))