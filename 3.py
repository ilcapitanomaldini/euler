import math
#6857
challengeNumber = 600851475143
maxDivisor = challengeNumber

def nextPrime(current):
    global maxDivisor
    current = current + 1
    while True:
        if isPrime(current):
            return current
        current = current + 1
    return -1

def isPrime(number):
    if number == 1:
        return False
    iterator = 2
    loopInvariantThatVaries = number
    while iterator < loopInvariantThatVaries:
        if number%iterator == 0:
            return False
        else:
            loopInvariantThatVaries = math.floor(number / iterator)
            iterator = iterator + 1
    return True
# Approach 1
"""
prime = 2
primeList = []
while prime <= maxDivisor:
    if prime in primeList:
        newValue = nextPrime(prime)
        prime = prime if newValue == -1 else newValue
        continue
    if challengeNumber%prime == 0:
        primeList.append(prime)
    else:
    maxDivisor = math.floor(challengeNumber / prime)
    if isPrime(maxDivisor) and challengeNumber%maxDivisor == 0: 
        primeList.append(maxDivisor)
    newValue = nextPrime(prime)
    prime = prime if newValue == -1 else newValue
primeList.sort()
print(primeList[len(primeList)-1])
print(primeList)
"""
#Approach-2:
iterator = 2
largestPrime = 2
takeMax = False
while iterator <= maxDivisor:
    if challengeNumber%iterator == 0:
        if isPrime(iterator):
            largestPrime = iterator
        maxDivisor = math.floor(challengeNumber / iterator)
        if isPrime(maxDivisor):
            takeMax = True
            break
    iterator = iterator + 1
if takeMax:
    print(maxDivisor)
else:
    print(largestPrime)
"""
#Approach-3: from SO, doesn't wprk for squares
n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print(n)
"""