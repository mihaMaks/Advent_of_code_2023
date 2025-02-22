a = [1, 2, 3]
b = ["ba", "ccc"]


def check(a, c):
    print(c)
    b = []
    for el in c:
        d = el.split("#")
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


print(check(a, b))
