def sum = 0

def getItemsInBoth = { line->
    def inBoth=[:]
    def comparmentLength = line.length()/2 as int
    def compartment2 = line.substring(comparmentLength)
    line.substring(0,comparmentLength).each{c->
        if (compartment2.indexOf(c)>=0){
            inBoth[c] = true
        }
    }
    return inBoth
}

int lowerOffset = (int)'a' - 1
int upperOffset = (int)'A' - 27
new File("input.txt").eachLine{ line->
    getItemsInBoth(line).each{c,v->
        if (c >= 'a') {
            sum+= (int)c - lowerOffset
        } else {
            sum+= (int)c - upperOffset
        }
    }
}
println ("sum of priorities: $sum")

