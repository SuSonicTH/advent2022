def WIN = 6
def DRAW = 3
def LOOSE = 0
def map = [
    A:[X:3+LOOSE ,Y:1+DRAW ,Z:2+WIN],
    B:[X:1+LOOSE ,Y:2+DRAW ,Z:3+WIN],
    C:[X:2+LOOSE ,Y:3+DRAW ,Z:1+WIN],
]
def score = 0
new File("input.txt").eachLine{ line->
    score+= map[line[0..0]][line[2..2]]
}
println "score: $score"

