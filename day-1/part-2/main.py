inFile = open('input.txt', 'r')
lines = inFile.readlines()
def getPassword(input):
    res = 0
    index = 50
    for rotation in input:
        direction = rotation[0]
        distance = int(rotation[1:])
        fullRotations = distance // 100
        remainingDistance = distance % 100
        res += fullRotations
        if direction == 'L':
            if index and index - remainingDistance <= 0:
                res += 1
            index = (index - distance) % 100
        else:
            if index + remainingDistance >= 100:
                res += 1
            index = (index + distance) % 100
    return res
print(getPassword(lines))
