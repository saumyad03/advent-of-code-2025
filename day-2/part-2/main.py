def isValid(num):
    numStr = str(num)
    for length in range(1, len(numStr) // 2 + 1):
        if len(numStr) % length: continue
        seqCount = len(numStr) // length
        isValid = False
        for seqNum in range(seqCount):
            for i in range(length):
                if numStr[i] != numStr[seqNum * length + i]: 
                    isValid = True
                    break
            if isValid: break
        if not isValid: return False
    return True

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