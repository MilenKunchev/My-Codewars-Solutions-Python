def recurrence(values):
    lowest_value = 1000000
    lowest_value_index = 0
    increases_elements_count = 0
    result = False
    for i in range(12):
        num = values[i]
        if num < lowest_value:
            lowest_value = num
            lowest_value_index = i
    for i in range(lowest_value_index, 11):
        if values[i] < values[i + 1]:
            increases_elements_count += 1
            if increases_elements_count == 3:
                result = True
                break

        else:
            increases_elements_count = 0

    return result


# print(recurrence([7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35]))
# print(recurrence([9.98, 8.56, 4.62, 1.16, 0.26, 0.37, 0.32, 1.02, 1.02, 0.99, 1.41, 2.35]))
# print(recurrence([12.57, 6.86, 1.86, 1.93, 0.60, 1.26, 0.99, 2.1, 0.70, 0.72, 0.88, 1.9]))
# print(recurrence([14.66, 3.14, 0.53, 0.58, 1.00, 1.26, 0.99, 2.1, 1.50, 2.53, 2.17, 2.50]))
# print(recurrence([12.85, 5.45, 1.37, 1.47, 0.73, 2.1, 2.50, 2.53, 2.17, 2.50, 3.25]))
