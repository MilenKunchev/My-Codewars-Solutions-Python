def get_pins(observed):
    def get_possible_digits(noted_pin):
        numbers = {
            1: {'1', '2', '4'},
            2: {'1', '2', '3', '5'},
            3: {'2', '6'},
            4: {'1', '5', '7'},
            5: {'2', '4', '5', '6', '8'},
            6: {'3', '5', '6', '9'},
            7: {'4', '7', '8'},
            8: {'8', '0'},
            9: {'8', '9', '6'},
            0: {'8'}
        }
        result = set()
        while noted_pin:
            digit = noted_pin % 10
            result |= numbers[digit]
            noted_pin //= 10

        return result

    def gen_pins(idx, pin, result, elements):
        if idx >= len(pin):
            result.append(''.join(pin))
            return
        for num in elements:
            pin[idx] = num
            gen_pins(idx + 1, pin, result, elements)
        return result

    possible_digits = get_possible_digits(observed)
    print(possible_digits)
    pin = [None] * len(str(observed))
    all_pins = gen_pins(0, pin, [], possible_digits)
    return sorted(all_pins)


print(sorted(get_pins(369)))
expected = sorted(
    ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368",
     "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698",
     "699", "298", "236", "239"])
print(expected)
# ["339","366","399","658","636","258","268","669","668","266","369","398","256",
# "296","259","368","638","396","238","356","659","639","666","359","336","299",
# "338","696","269","358","656","698","699","298","236","239"])]
