s = [1, 2, 3, 4, 5]

for i in range(len(s)):
    if i == 2:
        s.append(6)
    if i == 3:
        s.remove(5)

    print(s[i])
