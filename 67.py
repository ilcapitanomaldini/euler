with open("./AncillaryFiles/67.txt", "r") as file:
    data = file.readlines()
    rowCount = len(data)
    colCount = len(data[rowCount-1].split())
    dataMatrix = [[-1 for x in range(colCount)] for y in range(rowCount)] 
    for index, line in enumerate(data):
        rowIndex = index
        words = line.split()
        for colIndex, word in enumerate(words):
            dataMatrix[rowIndex][colIndex] = int(word)
print(rowCount, colCount)
for rowIndex in range(rowCount-2, -1, -1):
    for colIndex, colData in enumerate(dataMatrix[rowIndex]):
        if colData < 0:
            continue
        dataMatrix[rowIndex][colIndex] = dataMatrix[rowIndex][colIndex] + max(dataMatrix[rowIndex+1][colIndex],dataMatrix[rowIndex+1][colIndex+1])
print(dataMatrix[0][0]) #7273

