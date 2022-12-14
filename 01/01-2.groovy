def list=[]
def sum = 0
new File("input.txt").eachLine{ line->
    if (line.isEmpty()){
        list<<sum
        sum = 0
    } else {
        sum+=(line as int)
    }
}
def topThree=list.sort().reverse()[0..2].sum()
println "calories of top three: $topThree"

