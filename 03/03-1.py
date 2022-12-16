def inBoth(line):
    line = line.strip()
    half = int(len(line) / 2)
    compartment2 = line[half:]
    for c in line[0:half]:
        if (compartment2.find(c)>=0):
            return c
    
def getValue(char):
    if char >= 'a':
        return ord(char) - ord('a') + 1
    else:
        return  ord(char) - ord('A') + 27
    
sum = 0
with open('input.txt', 'r') as input:
    for line in input:
        char = inBoth(line)
        sum += getValue(char)

print(f"sum of priorities: {sum}")

