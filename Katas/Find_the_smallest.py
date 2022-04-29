def smallest(n):
    new_number = n
    old_index = 0
    new_index = 0
    for i in range(len(str(n))):
        numbers_list = [x for x in str(n)]
        digit = numbers_list.pop(i)

        for j in range(len(str(n))):
            numbers_list.insert(j, digit)
            number = int(''.join(numbers_list))
            if number < new_number:
                new_number = number
                old_index = i
                new_index = j
            numbers_list.pop(j)
    return [new_number, old_index, new_index]


print(smallest(321))  # [1432, 3, 0]
