num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

def containsZero(arrayString):
    if "0" in arrayString:
        return True
    else:
        return False

def summer(start, num, length):
    maxSum = 0
    """while start+length-1 < len(num):
        sum=0
        for loopIndex in range(start, start+length-1):
            sum=sum+
        start = start + 1
    """
    sum=0
    maxStart = 0
    while start+length < len(num):
        if sum == 0:
            for loopIndex in range(start, start+length):
                sum=sum+int(num[loopIndex])
        else:
            sum = sum - int(num[start-1]) + int(num[start+length-1])
        if containsZero(num[start:start+length-1]):
            start = start + 1
            continue
        if sum > maxSum:
            maxSum = sum
            maxStart = start
        start = start + 1
    return maxStart
startIndex = summer(0,num,13)
product = 1
for loopIndex in range(startIndex, startIndex+13):
    product=product*int(num[loopIndex])
print(len(num))
print(startIndex)
print(product)

def producer(start, num, length):
    maxProduct = 0
    product=1
    maxStart = 0
    skipped = True
    while start+length < len(num):
        if product == 1 or skipped:
            skipped = False
            for loopIndex in range(start, start+length):
                product=product*int(num[loopIndex])
        else:
            product = product / int(num[start-1]) * int(num[start+length-1])
        if containsZero(num[start:start+length-1]):
            skipped = True
            start = start + 1
            product = 1
            continue
        if product > maxProduct:
            maxProduct = product
            maxStart = start
        start = start + 1
    return maxStart
startIndex = producer(0,num,13)
product = 1
for loopIndex in range(startIndex, startIndex+13):
    product=product*int(num[loopIndex])
print(product)