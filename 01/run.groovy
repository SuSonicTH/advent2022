def max = 0
def sum = 0
new File("input.txt").eachLine{line->
    if (line.isEmpty()){
        if (sum > max) {
            max = sum
        }
        sum = 0
    } else {
        def current = line as int
        sum+=current
    }
}

println "max calories: $max"

