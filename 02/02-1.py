WIN = 6
DRAW = 3
LOOSE = 0
map = {
    "A":{"X":1+DRAW  ,"Y":2+WIN   ,"Z":3+LOOSE},
    "B":{"X":1+LOOSE ,"Y":2+DRAW  ,"Z":3+WIN},
    "C":{"X":1+WIN   ,"Y":2+LOOSE ,"Z":3+DRAW},
}
score = 0
with open('./02/input.txt', 'r') as input:
    for line in input:
        score+=map[line[0:1]][line[2:3]]
print(f"score: {score}")
