inFile = open('input.txt', 'r')
lines = inFile.readlines()
def getPassword(input):
    res = 0
    index = 50
    for rotation in input:
        direction = rotation[0]
        distance = int(rotation[1:])
        if direction == 'L':
            index = (index - distance) % 100
        else:
            index = (index + distance) % 100
        if index == 0:
            res += 1
    return res
print(getPassword(lines))