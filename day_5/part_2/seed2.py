f = open("../input.txt")
# f = open("test01.in")
lines = f.readlines()
seeds = []
maps = []
read = False
name = "zero"
names = []
for line in lines:
    if line == "\n" and name != "zero":
        # print(seeds, maps)
        rm = -1
        i = 0
        j = 0
        while i < len(seeds):
            s, e = seeds[i]

            for map in maps:
                md, ms, mr = map
                mr -= 1
                offset = map[0]-map[1]
                # print(seeds[i], map, offset)
                if s >= ms and e <= ms+mr:
                    seeds[i] = (s+offset, e+offset)
                    # print(1, seeds[i], map, offset)

                elif s < ms and e > ms+mr:
                    seeds.append((s, ms-1))
                    seeds.append((ms+mr+1, e))
                    seeds[i] = (ms+offset, ms+mr+offset)
                    # print(2, seeds[i], seeds[-2], seeds[-1], map, offset)

                elif s < ms and e >= ms and e <= ms+mr:
                    seeds.append((s, ms-1))
                    seeds[i] = (ms+offset, e+offset)
                    # print(3, seeds[-2], seeds[-1], map, offset)

                elif s >= ms and s <= ms+mr and e > ms+mr:
                    seeds.append((ms+mr+1, e))
                    seeds[i] = (s+offset, ms+mr+offset)
                    # print(4, seeds[-2], seeds[-1], map, offset)
            i += 1
        # print(seeds)
        # print(seeds, "\n")
        read = False
       # print(seeds)
        maps.clear()

    if read:
        nums = line.split(" ")
        n = []
        for i in nums:
            n.append(int(i))
        maps.append(n)

    if line.__contains__("map"):
        name = line.split(" ")[0]
        read = True

    if line.__contains__("seeds"):
        b, c = 0, 0
        j = 0
        for a in line.split():
            if a != "seeds:" and j % 2 == 0:
                b = int(a)
                j += 1
            elif a != "seeds:" and j % 2 == 1:
                c = int(a)
                j += 1
                seeds.append((b, b+c-1))
        # print(seeds)


# print(seeds)
print(min(seeds))
