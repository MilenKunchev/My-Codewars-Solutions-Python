def smallest(n):
    digits = list(str(n))
    m = len(digits)

    def second_is_bigger(digits, m):
        min_digit = "9"
        min_digit_index = -1
        next_smallest_digit = "9"
        next_smallest_digit_index = -1
        new_index = 0

        for i in range(m - 1, -1, -1):
            """ Find smallest digit"""
            digit = digits[i]

            if digit < min_digit and i > 0:
                min_digit = digit
                min_digit_index = i
                """ Find most left min digit if exist"""
                while min_digit_index > 0 and digits[min_digit_index - 1] == min_digit:
                    min_digit_index -= 1
        """ If smallest digit is 0  --> new index = 0"""

        if min_digit != "0":
            """ if smallest digit is bigger then zero find first digit bigger then smallest digit
                     and put smallest digit before it"""
            for i in range(m - 1):
                if min_digit == digits[i]:
                    """ Digit is equal to smallest digit --> insert smallest digit before existing digit"""
                    digits.pop(min_digit_index)
                    digits.insert(i, min_digit)
                    break
                if min_digit < digits[i]:
                    new_index = i
                    digits.pop(min_digit_index)
                    digits.insert(new_index, min_digit)
                    break
        else:
            digits.pop(min_digit_index)
            digits.insert(new_index, min_digit)

        number = "".join(digits)
        result = [int(number), min_digit_index, new_index]
        return result

    result = second_is_bigger(digits, m)

    return result

    # def second_is_smallest(digits):
    #     min_num = digits.pop(0)
    #     digit = int("".join(digits))
    #     digits = list(str(digit))
    #     m = len(digits)
    #     min_num_index = 0
    #     new_index = m
    #     for i in range(m):
    #         num = digits[i]
    #         if min_num < num:
    #             new_index = i
    #             if new_index == 0:
    #                 new_index = 1
    #             break
    #     digits.insert(new_index, min_num)
    #     number = "".join(digits)
    #     result = [int(number), min_num_index, new_index]
    #
    #     return result


# print(smallest(936075697141253875))  # [93675697141253875, 3, 0]
# print(smallest(199819884756))  # [119989884756, 4, 0]
# print(smallest(187863002809))  # [18786300289, 10, 0]
# print(smallest(65164125020641425))  # [6516412502641425, 10, 0]
# print(smallest(935722063368435968))  # [93572263368435968, 6, 0]
# print(smallest(269045))  # [26945, 3, 0]
# print(smallest(285365))  # [238565, 3, 1]
# print(smallest(199819884756))  # [119989884756, 4, 0]
# #
# print(smallest(337588310099269885))  # [33758831099269885, 8, 0]
# # #
# print(smallest(261235))  # [126235, 2, 0]
# #
# print(smallest(500524476335640833))  # [5244576335640833, 0, 6]
# print(smallest(903348281118728119))  # [33482811187281199, 0, 16]
# print(smallest(935855753))  # [358557539, 0, 8]
#
# print(smallest(613938516533535553))  # [136938516533535553, 0, 2]
# print(smallest(708215981654387226))  # [78215981654387226, 0, 1]

# 524554763356408533
# 5244576335640833
