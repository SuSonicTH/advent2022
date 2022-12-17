def isStart(s, string):
    for i in range(3):
        index = string.index(string[s + i], s + i + 1)
        if index > 0 and index < s + 4:
            return False
    return True


def getMarkerPosition(data):
    for i in range(len(data) - 4):
        if isStart(i, data):
            return i + 4


with open('input.txt', 'r') as file:
    data = file.read()

print(f"marker position {getMarkerPosition(data)}")
