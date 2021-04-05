#Collatz sequence
#525, 837799
chainLengths = [-1 for x in range(10000000)]
chainLengths[0] = -1 #trick
chainLengths[1] = 1

def isEven(number):
    return number%2==0

#Recursive approach, correct but ran into memory issues
"""
def sequencer(number):
    global chainLengths
    if (chainLengths[number] > -1):
        return chainLengths[number]
    if isEven(number):
        lastSequenced = sequencer(int(number/2))
        chainLengths[number] = lastSequenced + 1 
        return lastSequenced + 1
    else:
        lastSequenced = sequencer((3*number)+1)
        chainLengths[number] = lastSequenced + 1
        return lastSequenced + 1
"""
def iterativeSequencer(number):
    global chainLengths
    if (chainLengths[number] > -1):
        return chainLengths[number]
    chainLength = 0
    looper = number
    path = [number]
    limitExceededLooper = 0
    while chainLengths[looper] == -1:
        if limitExceededLooper > 0:
            looper = limitExceededLooper
            limitExceededLooper = 0
        #increment chain length
        chainLength = chainLength + 1
        if isEven(looper): 
            looper = int(looper/2)
        else:
            looper = (3*looper)+1
        path.append(looper)
        #don't store above limit results
        if looper > len(chainLengths):
            limitExceededLooper = looper
            looper = 0
    path.pop()
    #maintain the values of the chain generated
    for spot,stop in enumerate(path):
        if stop > len(chainLengths):
            continue
        chainLengths[stop] = chainLengths[looper] + chainLength - (spot)
    chainLengths[number] = chainLengths[looper] + chainLength
    return chainLengths[number]

#runner code
index = 2
maxVal = 0
maxValIndex = 0
while index < 1000000:
    if chainLengths[index] == -1:
        length = iterativeSequencer(index)
        if length > maxVal:
            maxVal = length
            maxValIndex = index 
    index = index + 1
print(maxVal, maxValIndex)