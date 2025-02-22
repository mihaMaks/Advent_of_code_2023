file = open("test3.in")
file = open("input.txt")
file = open("test6.in")
file = open("test2.in")
file = open("test1.in")

lines = file.readlines()
grid = []
# find S
sy = 0
sx = 0
for i in range(len(lines)):
    grid.append(list(lines[i]))
    if lines[i].__contains__("S"):
        sy = i
        sx = lines[i].find("S")


def get_position(pair, lines):
    y, x = pair
    return lines[y][x]


class Fork:
    def __init__(self, yx, prev):
        self.yx = yx
        self.prev = prev


def check_directions_s(position, map, lines, prev):
    ok_steps = []
    y, x = position
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if connected(position, i, j, map, lines, prev):
                ok_steps.append(Fork((y+j, x+i), position))
                print(ok_steps[-1].yx, get_position(ok_steps[-1].yx, lines))

    return ok_steps


def check_directions_p(position, map, lines, prev):
    ok_steps = []
    y, x = position
    for j, i in map[get_position(position, lines)]:
        # print("checking:", lines[y+j][x+i], (y+j, x+i))
        if connected(position, i, j, map, lines, prev):
            ok_steps.append(Fork((y+j, x+i), position))
            # print("avalible:", ok_steps[-1].yx,
            #     get_position(ok_steps[-1].yx, lines))

    return ok_steps


def connected(position, i, j, map, lines, prev):
    y, x = position
    maybe_y = y+j
    maybe_x = x+i
    if prev[0] == maybe_y and prev[1] == maybe_x:
        return False
    try:
        pipe_direction = map[lines[maybe_y][maybe_x]]
    except:
        print("index out")
        return False

    for vertical, horizontal in pipe_direction:
        if maybe_y+vertical == y and maybe_x+horizontal == x:
            return True
    return False


map = {"|": [(1, 0), (-1, 0)], "-": [(0, 1), (0, -1)], "L": [(-1, 0), (0, 1)], "J": [(-1, 0), (0, -1)],
       "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)], ".": [(0, 0), (0, 0)], "S": [(1, 0), (-1, 0), (0, 1), (0, -1)]}

forks = []
position = (sy, sx)
prev = (-1, -1)
steps = 0
simbol = "Z"
p_under_s = ""
while simbol != "S":
    # print("positioned:", simbol, position)
    if simbol == "Z":
        s_ok = []
        for f in check_directions_s(position, map, lines, prev):
            forks.append(f)
        for k in map.keys():
            for j, i in map[k]:
                if connected(position, i, j, map, lines, prev):
                    s_ok.append(Fork((sy+j, sx+i), position))
            if len(s_ok) == 2:
                p_under_s = k
                print(k)
                break
            else:
                s_ok.clear()

    else:
        for f in check_directions_p(position, map, lines, prev):
            forks.append(f)

    frk = forks.pop()
    prev = position
    next = frk.yx
    # forks.pop()
    # print(position[0], position[1])
    grid[position[0]][position[1]] = "X"
    position = next
    simbol = get_position(position, lines)
    steps += 1
print(steps/2)
grid[sy][sx] = p_under_s


count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "O" and grid[i][j] != "X":
            count += 1
        print(grid[i][j], end="")
    print("\n", end="")

print(count)
