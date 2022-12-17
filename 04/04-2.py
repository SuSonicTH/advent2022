def getSection(elve):
    section = elve.split('-')
    return {"start": int(section[0]), "end": int(section[1])}


def getSections(line):
    line = line.strip()
    elves = line.split(',')
    return getSection(elves[0]), getSection(elves[1])


def overlaps(section1, section2):
    return (section1["start"] >= section2["start"] and section1["start"] <= section2["end"]) \
        or (section1["end"] <= section2["end"] and section1["end"] >= section2["start"])


count = 0
with open('input.txt', 'r') as input:
    for line in input:
        section1, section2 = getSections(line)
        if overlaps(section1, section2) or overlaps(section2, section1):
            count += 1

print(f"count: {count}")
