def get_pins(observed):
    def get_possible_digits(noted_pin):
        possible = {
            '1': ['1', '2', '4'],
            '2': ['1', '2', '3', '5'],
            '3': ['2', '6'],
            '4': ['1', '5', '7'],
            '5': ['2', '4', '5', '6', '8'],
            '6': ['3', '5', '6', '9'],
            '7': ['4', '7', '8'],
            '8': ['8', '0', '5', '7', '9'],
            '9': ['8', '9', '6'],
            '0': ['0', '8']
        }
        result = []
        digits = str(noted_pin)
        for char in digits:
            result.append(possible[char])
        return result

    def gen_pins():
        return None

    possible_digits = get_possible_digits(observed)
    return get_possible_digits(observed)


print(get_pins(1911))
# expected = sorted(
#     ['20', '25', '27', '28', '29', '40', '45', '47', '48', '49', '50', '55', '57', '58',
#      '59', '60', '65', '67', '68', '69', '80', '85', '87', '88', '89'])
# print(expected)
