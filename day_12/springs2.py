import copy
f = open("input.txt")
f = open("test1.in")


# springs = []
# arrangements = []

springs2 = []
arrangements2 = []

for line in f.readlines():
    spring, arr = line.split()
    # spring, arr = line.split()
    spring *= 5
    print(spring)

    # springs.append(spring)
    t = [list(s) for s in spring.split(".") if len(s) > 0]

    y = [int(a) for a in arr.split(",")]
    y *= 5
    springs2.append(t)
    arrangements2.append(y)
    print(t, y)
    # springs.append([list(s) for s in spring.split(".") if len(s) > 0])
    # arrangements.append([int(a) for a in arr.split(",")])


def check(s, a):
    j = ["".join(i) for i in s]
    b = []
    for el in j:
        d = el.split(".")
        for e in d:
            if len(e) > 0:
                b.append(e)
    if len(a) == len(b):
        for i, k in zip(a, b):
            if len(k) != i:
                return 0
    else:
        return 0
    return 1


def rek(ix, si, g, deep, a):
    # s = copy.deepcopy(g)
    s = g
    sum = 0
    if si == len(s):
        if check(s, a):
            return 1
        return 0
    if ix == len(s[si]):
        return rek(0, si+1, s, deep+1, a)
    c = s[si][ix]
    if c == "?":
        # broken
        s[si][ix] = "#"
        sum += rek(ix+1, si, s, deep+1, a)
        # not broken
        s[si][ix] = "."
        sum += rek(ix+1, si, s, deep+1, a)
        s[si][ix] = "?"
    if c == "#":
        sum += rek(ix+1, si, s, deep+1, a)
    return sum


i = 0
res = 0
print(2**15)
for s, a in zip(springs2, arrangements2):
    # print(s, a)
    # print(rek(0, 0, s, 0, a))
    l = rek(0, 0, s, 0, a)
    print(i)
    res += l
    i += 1
print(res)
