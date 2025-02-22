import functools

# f = open("test.in")
f = open("input.txt")

lines = f.readlines()

hands = []


def checkHand(cards):
    value = [0]
    kind = 0
    jokers = cards.count('J')
    max = 0
    ix = 0
    j = 1
    for i in range(len(cards)):
        if cards[i] != 'J':
            kind = cards.count(cards[i])
            value.append(kind)
            # print(cards[i], kind)
            j = len(value)-1
        if kind > max:
            max = kind
            ix = j
    # print(value, ix)
    if jokers:
        value.append(jokers*value[ix] + jokers*(jokers+value[ix]))

    # print(value)
    return sum(value)


def comparator(cards1, cards2):
    c1 = checkHand(cards1[0])
    c2 = checkHand(cards2[0])
    m = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    if c1 == c2:
        for i in range(len(cards1[0])):
            a = cards1[0][i]
            b = cards2[0][i]
            if a != b:
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
    print(cards, checkHand(cards))


s = sorted(hands, key=functools.cmp_to_key(comparator))

res = 0
for i in range(1, len(s)+1):
    res += int(s[i-1][1])*i
print(res)
