def get_pins(observed):
    count_digits = len(str(observed))

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

    def gen_pins(idx, digits, pin, all_pins):
        if idx == count_digits:
            return
        for combination in digits:
            # TODO variations from nums in digits
            gen_pins(idx + 1, digits, pin, all_pins)

    possible_digits = get_possible_digits(observed)
    gen_pins(0, possible_digits, [], [])

    return None


print(get_pins(369))
# expected = sorted(
#     ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368",
#     "638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])

# print(expected)
