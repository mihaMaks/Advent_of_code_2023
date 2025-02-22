f = open("test1.in")

springs = []
arrangements = []

for line in f.readlines():
    spring, arr = line.split()
    # springs.append(spring)
    springs.append([s for s in spring.split(".") if len(s) > 0])
    arrangements.append([int(a) for a in arr.split(",")])


def rek(ix, si, ai, s, d, deep):
    a = d.copy()
    if ai >= len(a):
        return 0
    # rek ok
    if a[ai] == 0 and ai == len(a)-1 and si == len(s)-1 and ix == len(s[si]):
        print("rek ok")
        return 1
    # too far in springs
    if si == len(s):
        print("len(s) == si")
        return 0
    # too far in group
    if ix == len(s[si]):
        if a[ai] != 0:
            print("len(s[si] == ix)", "deep:", deep)
            return 0
        print("mached")
        print(s[si][ix-1], (si, ix-1))
        return rek(0, si+1, ai+1, s, a, deep+1)

    c = s[si][ix]

    q, w, e, r = 0, 0, 0, 0
    if c == "?":
        # not broken
        if a[ai] == 0:
            if ix+1 == len(s[si]):
                print("1 deep:", deep)
                print(c, (si, ix), ai)
                print(s[si][ix:], a)
                q = rek(0, si+1, ai+1, s, a, deep+1)
            else:
                print("2 deep:", deep)
                print(c, (si, ix), ai)
                print(s[si][ix:], a)
                q = rek(ix+1, si, ai, s, a, deep+1)
                print("2.5 deep:", deep)
                print(c, (si, ix), ai)
                print(s[si][ix:], a)
                r = rek(ix+1, si, ai+1, s, a, deep+1)

        else:
            print("3 deep:", deep)
            print(c, (si, ix), ai)
            print(s[si][ix:], a)
            q = rek(ix+1, si, ai, s, a, deep+1)  # 0 1
        # broken
        a[ai] -= 1
        print("4 deep:", deep)
        print(c, (si, ix), ai)
        print(s[si][ix:], a)
        w = rek(ix+1, si, ai, s, a, deep+1)  # 1

    if c == "#":
        a[ai] -= 1
        if a[ai] < 0:
            print("a[ai] < 0")
            return 0
        print("5 deep:", deep)
        print(c, (si, ix), ai)
        print(s[si][ix:], a)
        e = rek(ix+1, si, ai, s, a, deep+1)
    return q+w+e+r


i = 0

for s, a in zip(springs, arrangements):
    if i == 5:
        print(s, a)
        print(rek(0, 0, 0, s, a, 0))

        break
    i += 1
