def max = 0
def sum = 0
new File("input.txt").eachLine{ line->
    if (line.isEmpty()){
        if (sum > max) {
            max = sum
        }
        sum = 0
    } else {
        sum+=(line as int)
    }
}
println "max calories: $max"

