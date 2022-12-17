list = []
current_sum = 0
with open('input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        if line == "":
            list.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
list.sort(reverse=True)
top_three = sum(list[0:3])
print(f"calories of top three: {top_three}")
