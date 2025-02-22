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


f = open("test.in")
f = open("input.txt")
block = []
sum = 0
for line in f.readlines():
    if line == "\n":
        print(line)
        delna = 0
        grid_ver = check(block)
        for i in range(len(grid_ver[0])):
            ver = True
            for j in range(len(grid_ver)):
                if grid_ver[j][i] == 0:
                    ver = False
                    break
            if ver:
                delna += i+1

        grid_hor = check2(block)
        for i in range(len(grid_hor)):
            if grid_hor[i]:
                delna += 100*(i+1)
        print(delna)
        sum += delna
        block.clear()
    else:
        # print(line)
        strip = line.strip("\n")
        block.append(strip)

print(sum)
"""             
"""
