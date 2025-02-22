f = open("test1.in")
f = open("input.txt")
sequences = []

for line in f.readlines():
    nums = line.split()
    sequences.append([int(a) for a in nums])


def rek(seq):
    new = []
    c = 0
    for i in range(len(seq)-1):
        t = seq[i+1]-seq[i]
        if t == 0:
            c += 1
        new.append(t)
    print(seq, new)
    if c == len(new):
        # print("end:", new[-1])
        return seq[-1]
    r = seq[-1] + rek(new)
    print(r)
    return r


def rek2(seq):
    new = []
    c = 0
    for i in range(len(seq)-1):
        t = seq[i+1]-seq[i]
        if t == 0:
            c += 1
        new.append(t)
    print(seq)
    print(new)
    if c == len(new):
        # print("end:", new[-1])
        return seq[0]
    r = seq[0] - rek2(new)
    print(r)
    return r


sum = 0
for seq in sequences:
    # next_num = rek(seq)
    first_num = rek2(seq)
    sum += first_num
    # print(next_num)
print(sum)
