from itertools import product as pr


def get_pins(observed):

    def get_possible_digits(noted_pin):
        possible = {
            '1': ['1', '2', '4'],
            '2': ['1', '2', '3', '5'],
            '3': ['2', '3', '6'],
            '4': ['1', '4', '5', '7'],
            '5': ['2', '4', '5', '6', '8'],
            '6': ['3', '5', '6', '9'],
            '7': ['4', '7', '8'],
            '8': ['0', '5', '7', '8', '9'],
            '9': ['6', '8', '9'],
            '0': ['0', '8']
        }
        result = []
        digits = str(noted_pin)
        for char in digits:
            result.append(possible[char])
        return result

    list_of_pins = list()
    pins = list(pr(*get_possible_digits(observed)))
    for x in pins:
        list_of_pins.append(''.join(x))
    return list_of_pins


print(get_pins(369))
expected = sorted(
    ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298',
     '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396',
     '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']
)
print(expected == get_pins(369))
