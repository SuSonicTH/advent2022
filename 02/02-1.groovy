def WIN = 6
def DRAW = 3
def LOOSE = 0
def map = [
    A:[X:1+DRAW  ,Y:2+WIN   ,Z:3+LOOSE],
    B:[X:1+LOOSE ,Y:2+DRAW  ,Z:3+WIN],
    C:[X:1+WIN   ,Y:2+LOOSE ,Z:3+DRAW],
]
def score = 0
new File("./02/input.txt").eachLine{ line->
    score+=map[line[0..0]][line[2..2]]
}
println "score: $score"

