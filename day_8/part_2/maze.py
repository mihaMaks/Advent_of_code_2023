import math

# f = open("test2.in")
f = open("test1.in")
f = open("input.txt")


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


lines = f.readlines()
instructoins = lines[0].strip()
map = {}
for i in range(2, len(lines)):
    node, connections = lines[i].split("=")
    conl, conr = connections.strip().split(" ")
    map.update({node.strip(): (conl.strip("(").strip(","), conr.strip(")"))})
    print(node.strip(), conl.strip("(").strip(
        ",").strip(), conr.strip(")").strip())

signs = [k for k in map.keys() if k.__contains__("A")]
nodes = [map[n] for n in signs]
moves = []
mod = len(instructoins)
print("AAA")
move = 0
for sign, node in zip(signs, nodes):
    move = 0
    while not sign.__contains__("Z"):
        turn = instructoins[move % mod]
        print(turn)
        if turn == "R":
            print(node[1])
            sign = node[1]
            node = map[node[1]]
        if turn == "L":
            print(node[0])
            sign = node[0]
            node = map[node[0]]
        move += 1
        print("moves", moves)
    moves.append(move)

res = moves[0]
for i in range(1, len(moves)):
    res = math.lcm(res, moves[i])


print(res)
