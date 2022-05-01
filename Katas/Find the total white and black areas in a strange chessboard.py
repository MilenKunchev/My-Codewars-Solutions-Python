def white_black_areas(cs, rs):
    s_white = 0
    s_black = 0

    even_row_sum = 0
    odd_row_sum = 0

    for i in range(0, len(cs), 2):
        even_row_sum += cs[i]

    for i in range(1, len(cs), 2):
        odd_row_sum += cs[i]

    for i in range(0, len(rs), 2):
        s_white += rs[i] * even_row_sum

    for i in range(1, len(rs), 2):
        s_white += rs[i] * odd_row_sum

    for i in range(0, len(rs), 2):
        s_black += rs[i] * odd_row_sum

    for i in range(1, len(rs), 2):
        s_black += rs[i] * even_row_sum

    return s_white, s_black

print(white_black_areas([3, 1, 2, 7, 1], [1, 8, 4, 5, 2]))

# print(white_black_areas([3, 1, 2, 7, 1, 11, 12, 3, 8, 1,5,5,6,7,8], [3, 1, 2, 7, 1, 11, 12, 3, 8, 1,5,5,6,7,8]))
