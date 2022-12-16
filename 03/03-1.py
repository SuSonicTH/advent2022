def inBoth(line):
    line = line.strip()
    half = int(len(line) / 2)
    compartment2 = line[half:]
    for c in line[0:half]:
        if (compartment2.find(c)>=0):
            return c
            
sum = 0     
with open('input.txt', 'r') as input:
    for line in input:
        char = inBoth(line)
        print(f"{char} {ord(char)} {ord('a')}")
        if char >= 'a':
            sum+= ord(char) - ord('a') + 1
        else:
            sum+= ord(char) - ord('A') + 27

print(f"sum of priorities: {sum}")

