def inAll(tripple):
    for c in tripple[0]:
        if (tripple[1].find(c)>=0 and tripple[2].find(c)>=0):
            return  c


def getValue(char):
    if char >= 'a':
        return ord(char) - ord('a') + 1
    else:
        return  ord(char) - ord('A') + 27

sum = 0
index = 0
tripple = []
with open('input.txt', 'r') as input:
     for line in input:
        tripple.append(line)
        index+=1
        if index%3 == 0 :
            char = inAll(tripple)
            sum+= getValue(char)
            tripple=[]
        
print(f"sum of priorities: {sum}")

