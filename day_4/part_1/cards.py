import numpy as np

f = open("../input.txt")
# f = open("test.in")


lines = f.readlines()
sum = 0
deck = 0
# print(len(lines))
copies = np.ones(len(lines))
i = 0
for line in lines:
    forward = 1
    numbers = line.split(": ")[1]
    both = numbers.split("|")
    winning = set()
    for a in both[1].split(" "):
        if len(a) > 0:
            winning.add(int(a))
    my_nums = [int(a) for a in both[0].split(" ") if len(a) > 0]
    value = 0
    for n in my_nums:
        if n in winning:
            forward += 1
            if value == 0:
                value = 1
            else:
                value *= 2
    for s in range(1, forward):
        copies[i+s] += copies[i]

    # print(forward)
    sum += value
    forward -= 1
    i += 1


for i in copies:
    # print(i)
    deck += i
print(deck)
print(sum)
