from collections import deque


def line_up(hints):
    indexes = {}
    elements = deque()
    for hint in hints:
        elements.append(make_pair(hint))

    while elements:
        first, second = elements.pop()
        if not indexes:
            indexes[second] = 0
            indexes[first] = -1
            continue

        if first in indexes:
            indexes[second] = indexes[first] + 1
        if second in indexes:
            indexes[first] = indexes[second] - 1
        else:
            elements.appendleft((first, second))

    return [k for k, v in sorted(indexes.items(), key=lambda kvp: kvp[1])]


def make_pair(hint):
    elements = hint.split(' ')
    side = elements[-1]
    if side == "left":
        return elements[2], elements[0]
    return elements[0], elements[2]


print(line_up(["white has black on his left",
               "red has green on his right",
               "black has green on his left"]))

print(line_up(["d has c on his left",
               "c has b on his left",
               "b has a on his left"]))

print(line_up(["d has c on his right",
               "c has b on his right",
               "b has a on his right"]))

print(line_up(["green has pink on his left",
               "green has white on his right",
               "black has red on his right",
               "red has blue on his right",
               "black has white on his left"]))
# ["red", "green", "black", "white"]
# ["a", "b", "c", "d"]
# ['d', 'c', 'b', 'a']
# ['pink', 'green', 'white', 'black', 'red', 'blue']
