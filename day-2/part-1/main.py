def isValid(num):
    numStr = str(num)
    if len(numStr) % 2 == 1: return True
    for i in range(len(numStr) // 2):
        if numStr[i] != numStr[len(numStr) // 2 + i]:
            return True
    return False

def countInvalid(inp):
    res = 0
    ranges = inp.split(',')
    for r in ranges:
        start, end = r.split('-')
        for num in range(int(start), int(end) + 1):
            if not isValid(num): res += num
    return res

inFile = open('input.txt', 'r')
inp = inFile.read()
print(countInvalid(inp))