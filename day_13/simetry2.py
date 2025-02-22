def check(block):
    grid = []
    for strip in block:
        l = len(strip)
        g = []
        for i in range(l-1):
            simetric = True
            for j in range(1, int(l/2)+1):
                if i-j+1 < 0 or i+j >= l:
                    break
                # print(i-j+1, i+j)
                # print(line[i-j+1], line[i+j])
                if strip[i-j+1] != strip[i+j]:
                    simetric = False
                    break
            # print(i, simetric)
            if simetric:
                g.append(1)
            else:
                g.append(0)
        print(g)
        grid.append(g)
    return grid


def check2(block):
    l = len(block)
    g = []
    for i in range(l-1):
        simetric = True
        for j in range(1, int(l/2)+1):
            if i-j+1 < 0 or i+j >= l:
                break
            # print(i-j+1, i+j)
            # print(line[i-j+1], line[i+j])
            if block[i-j+1] != block[i+j]:
                simetric = False
                break
        # print(i, simetric)
        if simetric:
            g.append(1)
        else:
            g.append(0)
    print(g)
    return g


def izracunaj(grid_ver, column_to_check):
    delna1 = 0
    for i in range(len(grid_ver[0])):
        ver = True
        x = 0
        m = 0
        for j in range(len(grid_ver)):
            if grid_ver[j][i] == 0:
                x = j
                ver = False
            else:
                m += 1
        if m == len(grid_ver)-1:
            column_to_check.append((x, i))  # row, simetry line index
        if ver:
            delna1 += i+1
    return delna1


def izracunaj2(grid_ver, grid_ver_orig):
    delna1 = 0
    column_to_check = []
    for i in range(len(grid_ver[0])):
        ver = True
        x = 0
        m = True
        for j in range(len(grid_ver)):
            if grid_ver[j][i] == 0:
                x = j
                ver = False
            if grid_ver_orig[j][i] == 0:
                m = False
        if ver and not m:
            delna1 += i+1
    return delna1


f = open("test.in")
f = open("input.txt")
block = []
sum = 0
sum2 = 0
for line in f.readlines():
    if line == "\n":
        print(line)
        delna2 = 0
        grid_ver = check(block)
        column_to_check = []
        delna1 = izracunaj(grid_ver, column_to_check)
        print(delna1)
        first = False
        grid_ver2 = []
        while len(column_to_check) > 0:
            print(column_to_check)
            y, x = column_to_check.pop()
            for i in range(len(block[y])):
                b = block[y][i]
                if block[y][i] == "#":
                    block[y][i] = "."
                else:
                    block[y][i] = "#"
                grid_ver2 = check(block)
                print()
                delna2 = izracunaj2(grid_ver2, grid_ver)
                block[y][i] = b
                if delna1 != delna2 and delna2 != 0:
                    first = True
                    print("delna razlicna", delna1, delna2)
                    break
        grid_hor = check2(block)
        for i in range(len(grid_hor)):
            if grid_hor[i]:
                delna1 += 100*(i+1)
        if not first:
            grid_hor2 = []
            for i in range(len(block)):
                stop = False
                for j in range(len(block[0])):
                    delna2 = 0
                    b = block[i][j]
                    if block[i][j] == "#":
                        block[i][j] = "."
                    else:
                        block[i][j] = "#"
                    grid_hor2 = check2(block)
                    block[i][j] = b
                    for x in range(len(grid_hor2)):
                        if grid_hor2[x] and not grid_hor[x]:
                            delna2 += 100*(x+1)
                    if 0 != delna2 and delna1 != delna2:
                        print("delna razlicna", delna1, delna2)
                        stop = True
                        break
                if stop:
                    break

        print(delna1)
        sum += delna1
        sum2 += delna2
        block.clear()
    else:
        # print(line)
        strip = list(line.strip("\n"))
        block.append(strip)

print(sum)
print(sum2)
"""             
"""
