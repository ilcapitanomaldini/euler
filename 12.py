startIndex = 500000
#Approach1
"""
def triangleNumber(index):
    return int(index * (index + 1) / 2)
def factorCount(number):
    factorHolder = [False] * number
    factorHolder[0] = False
    factorHolder[1] = True
    index = 2
    counter = 1
    while index*index < number:
        if factorHolder[index] == False and number % index == 0 :
            counter = counter + 2
            factorHolder[index] = True
            factorHolder[int(number/index)] = True
        index = index + 1
    return counter

while True:
    if factorCount(triangleNumber(startIndex)) >= 500:
        print(triangleNumber(startIndex))
        break
    startIndex = startIndex + 1
"""
#Approach 2
import math

def getFactors(n):
    return sum(2 for i in range(1, round(math.sqrt(n)+1)) if not n % i)

def generateTriangles(limit):
    l = 1
    while l <= limit:
        yield sum(range(l + 1))
        l += 1

def testTriangles():
    triangles = generateTriangles(100000)
    for i in triangles:
        if getFactors(i) > 499:
            return i
print(testTriangles())