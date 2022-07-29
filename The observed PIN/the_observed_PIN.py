def get_pins(observed):
    result = []

    def get_possible_digits(observed):
        nums = set()
        while observed:
            digit = observed % 10
            nums.add(digit)

            if digit == 8:
                nums.add(0)
            if digit + 1 < 10:
                nums.add(digit + 1)
            if digit - 1 > 0:
                nums.add(digit - 1)
            if digit + 3 < 10:
                nums.add(digit + 3)
            if digit - 3 > 0:
                nums.add(digit - 3)
            observed //= 10
        return nums

    possible_digits = get_possible_digits(observed)

    return possible_digits


print(get_pins(11))
