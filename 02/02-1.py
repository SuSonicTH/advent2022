WIN = 6
DRAW = 3
LOOSE = 0
map = {
    "A": {"X": 1 + DRAW, "Y": 2 + WIN, "Z": 3 + LOOSE},
    "B": {"X": 1 + LOOSE, "Y": 2 + DRAW, "Z": 3 + WIN},
    "C": {"X": 1 + WIN, "Y": 2 + LOOSE, "Z": 3 + DRAW},
}
with open('input.txt', 'r') as input:
    score = sum([map[line[0:1]][line[2:3]] for line in input.readlines()])
print(f"score: {score}")
