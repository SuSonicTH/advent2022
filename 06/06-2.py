marker_lenght = 14


def isStart(s, string):
    for i in range(marker_lenght - 1):
        index = string.index(string[s + i], s + i + 1)
        if index > 0 and index < s + marker_lenght:
            return False
    return True


def getMarkerPosition(data):
    for i in range(len(data) - marker_lenght):
        if isStart(i, data):
            return i + marker_lenght


with open('input.txt', 'r') as file:
    data = file.read()

print(f"marker position {getMarkerPosition(data)}")
