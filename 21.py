#init empty 2d array
divisorCache = []
for i in range (0, 10001): 
    new = [] 
    divisorCache.append(new)

loopEnder = 10001
amicableSum = 0
for index in range(1,loopEnder):
    product = 2
    while product*index < loopEnder:
        number = index*product
        divisorCache[number].append(index)
        product = product + 1
    divisorSum = sum(divisorCache[index])
    #amicable logic
    if divisorSum < index and sum(divisorCache[divisorSum]) == index:
        amicableSum = amicableSum + index + divisorSum
print(amicableSum) #31626

    