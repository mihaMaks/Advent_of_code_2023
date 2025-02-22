f = open("test2.in")
f = open("test.in")
f = open("input.txt")

lines = f.readlines()
instructoins = lines[0].strip()
moves = 0
map = {}
for i in range(2, len(lines)):
    node, connections = lines[i].split("=")
    conl, conr = connections.strip().split(" ")
    map.update({node.strip(): (conl.strip("(").strip(","), conr.strip(")"))})
    print(node.strip(), conl.strip("(").strip(
        ",").strip(), conr.strip(")").strip())

node = map["AAA"]
sign = "AAA"
mod = len(instructoins)
print("AAA")
while sign != "ZZZ":
    turn = instructoins[moves % mod]
    print(turn)
    if turn == "R":
        print(node[1])
        sign = node[1]
        node = map[node[1]]
    if turn == "L":
        print(node[0])
        sign = node[0]
        node = map[node[0]]
    moves += 1
    print("moves", moves)

"""
"""
print(moves)
