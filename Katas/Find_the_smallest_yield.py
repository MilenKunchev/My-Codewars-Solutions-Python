def smallest(n):
    def moves(n):
        for i in range(len(str(n))):
            numbers_list = [x for x in str(n)]
            digit = numbers_list.pop(i)

            for j in range(len(str(n))):
                numbers_list.insert(j, digit)
                number = int(''.join(numbers_list))
                yield [number, i, j]
                numbers_list.pop(j)

    return min(moves(n))


print(smallest(321))  # [1432, 3, 0]
