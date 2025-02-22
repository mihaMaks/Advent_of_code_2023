f = open("input.txt", "r")
lines = f.readlines()
numbers = ["one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0
for line in lines:
    k = 0
    last = 0
    print(line.strip("\n"))
    for n, x in zip(numbers, digits):
        line = line.replace(n, n+str(x)+n)
    for c in line:
        if c.isdigit() and k == 0:
            k = int(c)
            last = k
        if c.isdigit():
            last = int(c)
    k *= 10
    k += last
    sum += k
    print("end:", k)

print(sum)
