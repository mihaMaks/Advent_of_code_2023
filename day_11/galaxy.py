file = open("test1.in")
file = open("input.txt")

lines = file.readlines()
y_expansions = []
x_expansions = []
galaxies = []
for y in range(len(lines)):
    empty = True
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            empty = False
            galaxies.append((y, x))
    if empty:
        y_expansions.append(y)

for i in range(len(lines[0])-1):
    empty = True
    for j in range(len(lines)):
        if lines[j][i] == "#":
            empty = False
    if empty:
        x_expansions.append(i)

# print(x_expansions, y_expansions)
# print(galaxies)


def sum_expansions(range, expansions):
    a, b = range
    sum = 0
    for e in expansions:
        if a <= e and e <= b:
            sum += 999999
    return sum


res = 0
for i in range(len(galaxies)-1):
    print(i+1, "galaxy")
    for j in range(i+1, len(galaxies)):
        distance = 0
        g1 = galaxies[i]
        g2 = galaxies[j]
        print(g1, g2)

        range_x = ((min(g1[1], g2[1]), max(g1[1], g2[1])))
        range_y = ((min(g1[0], g2[0]), max(g1[0], g2[0])))
        distance += abs(g1[1] - g2[1]) + sum_expansions(range_x, x_expansions)
        distance += abs(g1[0] - g2[0]) + sum_expansions(range_y, y_expansions)
        print(distance)
        res += distance
"""
"""
print(res)
