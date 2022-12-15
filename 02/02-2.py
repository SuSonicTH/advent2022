WIN = 6
DRAW = 3
LOOSE = 0
map = {
    "A":{"X":3+LOOSE ,"Y":1+DRAW ,"Z":2+WIN},
    "B":{"X":1+LOOSE ,"Y":2+DRAW ,"Z":3+WIN},
    "C":{"X":2+LOOSE ,"Y":3+DRAW ,"Z":1+WIN},
}
with open('input.txt', 'r') as input:
    score = sum( [map[line[0:1]][line[2:3]] for line in input.readlines()])
print(f"score: {score}")
