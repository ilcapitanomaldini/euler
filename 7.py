#10001st index in list of primes.
#Attempt at sieve-like algorithm
needIndex = 10001
primeList = []
isPrime = [True] * 1000000
#numberList
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

index = 0
while index < len(isPrime):
    if isPrime[index]:
        primeList.append(index)
    index = index + 1

print(primeList[needIndex-1])
#print(primeList)

