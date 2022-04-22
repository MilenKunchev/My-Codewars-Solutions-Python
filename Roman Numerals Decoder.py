def solution(roman):
    result = 0
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    numbers = [nums[x] for x in roman]

    while numbers:
        number = numbers.pop()
        if numbers and number > numbers[-1]:
            number -= numbers.pop()
        result += number
    return result


# print(solution("XXI"))
# print(solution("I"))
# print(solution("IV"))
# print(solution("MMVIII"))
# print(solution("XLIX"))
