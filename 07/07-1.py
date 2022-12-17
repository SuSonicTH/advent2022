import pprint

tree = {}
ctree = tree
with open('input.txt', 'r') as input:
    for line in input:
        line = line.strip()
        if line == "$ cd /" or line == "$ ls":
            continue
        elif line.startswith("$ cd"):
            ctree = ctree[line[5:]]
        elif line.startswith("dir"):
            ctree[line[4:]] = {".": [], "..": ctree}
        else:
            items = line.split()
            ctree["."].append({"name": items[1], "size": int(items[0])})

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tree)
