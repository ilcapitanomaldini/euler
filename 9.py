a = 0
b = 1
c = 999
def pythagoreanTriplet():
    global a,b,c
    while True:
        a = 1
        while c > a:
            b = 1000 - (a + c)
            if b == 0:
                break
            if pow(a,2) + pow(b,2) == pow(c,2):
                    print("Reached")
                    return
            a = a + 1
        c = c - 1

pythagoreanTriplet()
print(a)
print(b)
print(c)
print(a*b*c)