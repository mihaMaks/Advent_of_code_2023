import functools

f = open("test.in")
# f = open("input.txt")

lines = f.readlines()

hands = []


def checkHand(cards):
    value = []
    kind = 0
    for c in cards:
        kind = cards.count(c)
        value.append(kind)
    return sum(value)


def comparator(cards1, cards2):
    c1 = checkHand(cards1[0])
    c2 = checkHand(cards2[0])
    m = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
    if c1 == c2:
        for i in range(len(cards1[0])):
            a = cards1[0][i]
            b = cards2[0][i]
            if a != b:
                print(a, b)
                if a in m.keys():
                    a = m[a]
                else:
                    a = int(a)
                if b in m.keys():
                    b = m[b]
                else:
                    b = int(b)
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0

    if c1 < c2:
        return -1
    elif c1 > c2:
        return 1
    else:
        return 0


for line in lines:
    cards, bid = line.split()
    hands.append((cards, bid))

   # print(cards, checkHand(cards))

s = sorted(hands, key=functools.cmp_to_key(comparator))
for a in s:
    print(a[0], checkHand(a[0]))

res = 0
for i in range(1, len(s)+1):
    res += int(s[i-1][1])*i
print(res)
