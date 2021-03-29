def sievePrimer(maxNum):
    isPrime = [True] * maxNum
    isPrime[0] = False
    isPrime[1] = False
    index = 2
    while index*index < len(isPrime):
        if isPrime[index] == True:
            innerIndex = index*index
            while innerIndex < len(isPrime):
                isPrime[innerIndex] = False
                innerIndex = innerIndex + index
        index = index + 1
    return isPrime

primeList = sievePrimer(2000000)
index = 0
sum = 0
while index < len(primeList):
    if primeList[index]:
        sum = sum + index
    index = index + 1

print(sum) #142913828922