with open("./AncillaryFiles/13.txt", "r") as file:
    data = file.readlines()
    rowCount = len(data)
    dataMatrix = [0 for x in range(rowCount)] 
    for index, line in enumerate(data):
        dataMatrix[index] = int(line)
    
#Brute
"""sum = 0
for data in dataMatrix:
    sum = sum + data
print(str(sum)[:10])
"""
#Approach 2
tenDigitWindow = [0 for x in range(10)]
carry=0
for horizontalLooper in range(len(str(dataMatrix[0]))):
    sumVal=carry
    for index, number in enumerate(dataMatrix):
        #sumVal=sumVal+(number%(pow(10, horizontalLooper + 1)))
        sumVal=sumVal+ (number // 10**(horizontalLooper) % 10)
    tenDigitWindow.pop(0)
    unit = sumVal%10
    carry = int((sumVal-unit)/10)
    #print("sum "+str(sumVal), "carry "+str(carry))
    tenDigitWindow.append(unit)
tenDigitWindow.pop(0)
tenDigitWindow.append(carry)
tenDigitWindow.reverse()
print(tenDigitWindow)
