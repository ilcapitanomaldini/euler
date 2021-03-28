largestPrime = 19
primeList = [2,3,4,5,7,9,11,13,16,17,19,20]
counter = 2
foundIt = True
while True:
    smallestMultiple = largestPrime * counter
    foundIt = True
    for prime in primeList:
        if smallestMultiple % prime == 0:
            continue
        else :
            foundIt = False
    if foundIt:
        print(smallestMultiple)
        raise SystemExit(smallestMultiple)
    counter = counter + 2

