# largest 2 digit palindrome = 9009 = 91* 99
import math

def palindromeLooper():
    maxDrome = 0
    outerLooper = 999
    while outerLooper > 500:
        innerLooper = outerLooper
        while innerLooper > 500:
            product = outerLooper*innerLooper
            if isPalindrome(product):
                maxDrome = product if product > maxDrome else maxDrome
            innerLooper = innerLooper - 1
        outerLooper = outerLooper - 1
    return maxDrome

def rev(num): 
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10)) 

def isPalindrome(product):
    return True if product == rev(product) else False

print(palindromeLooper())
