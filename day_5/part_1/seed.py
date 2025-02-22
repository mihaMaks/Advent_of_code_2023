# f = open("test01.in")
f = open("../input.txt")
lines = f.readlines()
seeds = []
maps = []
read = False
name = "zero"
names = []
for line in lines:
    if line == "\n" and name != "zero":
        # print(seeds, maps)
        for i in range(len(seeds)):
            for map in maps:
                offset = map[0]-map[1]
                if seeds[i] in range(map[1], map[1]+map[2]):
                    seeds[i] += offset
                    break
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
        seeds = [int(a) for a in line.split(" ") if a != "seeds:"]

print(seeds, maps)
for i in range(len(seeds)):
    for map in maps:
        offset = map[0]-map[1]
        if seeds[i] in range(map[1], map[1]+map[2]):
            seeds[i] += offset
            break

print(seeds)
print(min(seeds))
