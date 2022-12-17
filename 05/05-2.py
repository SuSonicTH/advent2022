# [J]             [F] [M]
# [Z] [F]     [G] [Q] [F]
# [G] [P]     [H] [Z] [S] [Q]
# [V] [W] [Z] [P] [D] [G] [P]
# [T] [D] [S] [Z] [N] [W] [B] [N]
# [D] [M] [R] [J] [J] [P] [V] [P] [J]
# [B] [R] [C] [T] [C] [V] [C] [B] [P]
# [N] [S] [V] [R] [T] [N] [G] [Z] [W]
# 1   2   3   4   5   6   7   8   9 

state = [
    ["N", "B", "D", "T", "V", "G", "Z", "J", ],
    ["S", "R", "M", "D", "W", "P", "F", ],
    ["V", "C", "R", "S", "Z", ],
    ["R", "T", "J", "Z", "P", "H", "G", ],
    ["T", "C", "J", "N", "D", "Z", "Q", "F", ],
    ["N", "V", "P", "W", "G", "S", "F", "M", ],
    ["G", "C", "V", "B", "P", "Q", ],
    ["Z", "B", "P", "N"],
    ["W", "P", "J", ],
]


def doMove(move, pos, to):
    source = state[pos]
    destination = state[to]
    crane = []
    for i in range(move):
        crane.append(source.pop())
    for i in range(len(crane)):
        state[to].append(crane.pop())


with open('input.txt', 'r') as input:
    for line in input:
        move = line.strip().split()
        doMove(int(move[1]), int(move[3]) - 1, int(move[5]) - 1)

topCrates = ""
for stack in state:
    topCrates += stack.pop()

print(f"topCrates: {topCrates}")
