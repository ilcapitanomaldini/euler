import enum

with open("./AncillaryFiles/11.txt", "r") as file:
    data = file.readlines()
    colCount = len(data[0].split())
    rowCount = len(data)
    dataMatrix = [[0 for x in range(colCount)] for y in range(rowCount)] 
    for index, line in enumerate(data):
        rowIndex = index
        words = line.split()
        for colIndex, word in enumerate(words):
            dataMatrix[rowIndex][colIndex] = int(word)
#print(dataMatrix)
def productRight(dataMatrix, rowIndex, colIndex, count):
    product = 1
    stopIndex = colIndex + count
    while colIndex < stopIndex:
        #print(rowIndex, colIndex)
        product = dataMatrix[rowIndex%len(dataMatrix)][colIndex%len(dataMatrix[0])] * product
        colIndex = colIndex + 1
    return product

def productDown(dataMatrix, rowIndex, colIndex, count):
    product = 1
    stopIndex = rowIndex + count
    while rowIndex < stopIndex:
        product = dataMatrix[rowIndex%len(dataMatrix)][colIndex%len(dataMatrix[0])] * product
        rowIndex = rowIndex + 1
    return product

def productSlide(dataMatrix, rowIndex, colIndex, count):
    product = 1
    stopIndex = colIndex + count
    while colIndex < stopIndex:
        product = dataMatrix[rowIndex%len(dataMatrix)][colIndex%len(dataMatrix[0])] * product
        colIndex = colIndex + 1
        rowIndex = rowIndex + 1
    return product

def productSlideLeft(dataMatrix, rowIndex, colIndex, count):
    product = 1
    stopIndex = rowIndex + count
    while rowIndex < stopIndex:
        product = dataMatrix[rowIndex%len(dataMatrix)][colIndex%len(dataMatrix[0])] * product
        colIndex = colIndex - 1
        rowIndex = rowIndex + 1
        if colIndex < 0:
            colIndex = colIndex + len(dataMatrix[0])
    return product

maxProduct = 1
for rowMover in range(0, len(dataMatrix)):
    for colMover in range(0,len(dataMatrix[rowMover])):
        rightProduct = productRight(dataMatrix, rowMover, colMover, 4)
        downProduct = productDown(dataMatrix, rowMover, colMover, 4)
        slideProduct = productSlide(dataMatrix, rowMover, colMover, 4)
        slideLeftProduct = productSlideLeft(dataMatrix, rowMover, colMover, 4)
        maxProduct = max(rightProduct, downProduct, slideProduct, slideLeftProduct, maxProduct) 

print(maxProduct) #70600674