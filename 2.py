evenSum = 0
def fibonacciGenerator(seed1, seed2, stopper, generatedAction):
    fibNumber = 0
    while fibNumber <= stopper:
        seed2 = seed1 + seed2
        seed1 = seed2 - seed1
        fibNumber = seed2
        generatedAction(seed2)
    

def isEven(number):
    return number % 2 == 0

def evenAdder(number):
    global evenSum 
    if isEven(number):
        evenSum = evenSum + number

evenAdder(1)
evenAdder(2)
fibonacciGenerator(1,2,4000000, evenAdder)
print(evenSum)

# Better solution is to either
    # 1. Observe pattern 1 1 2 3 5 8 13 21 34 55 89 144 ... where every third number is even.
    # 2. If we observe only the even numbers 2 8 34 144..., it follows the recursive relation. 