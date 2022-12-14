max = 0
sum = 0
with open('input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        if line == "" :
            if sum > max:
                max = sum
            sum = 0
        else:
            sum+= int(line)
print(f"max calories: {max}")

