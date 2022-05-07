def is_incrementing(number):
    return str(number) in '1234567890'


def is_decrementing(number):
    return str(number) in '9876543210'


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def is_followed_by_zeros(number):
    return set(str(number)[1:]) == set('0')


def is_interesting(number, awesome_phrases):
    tests = (is_incrementing, is_decrementing, is_palindrome,
             is_followed_by_zeros, awesome_phrases.__contains__)

    if number >= 100 and any(test(number) for test in tests):
        return 2
    if number + 1 >= 99 and any(test(number + 1) for test in tests):
        return 1
    if number + 2 >= 100 and any(test(number + 2) for test in tests):
        return 1
    return 0

# # "boring" numbers
# print(is_interesting(97, [1337, 256])) #0
# print(is_interesting(3, [1337, 256]))  # 0
# print(is_interesting(3236, [1337, 256]))  # 0
# #
# # progress as we near an "interesting" number
# print(is_interesting(11207, []))  # 0
# print(is_interesting(11208, []))  # 0
# print(is_interesting(11209, []))  # 1
# print(is_interesting(11210, []))  # 1
# print(is_interesting(11211, []))  # 2
#
# # nearing a provided "awesome phrase"
# print(is_interesting(1335, [1337, 256]))  # 1
# print(is_interesting(1336, [1337, 256]))  # 1
# print(is_interesting(1337, [1337, 256]))  # 2
