#NOTE: Redo with external sorting algorithm
import re
def getIntVal(character):
    #since all caps
    return ord(character) - ord("A") + 1

def getSummedIntVal(tuple):
    index, string = tuple
    values = map(getIntVal, string)
    return (index+1)*sum(values)

with open("./AncillaryFiles/22.txt", "r") as file:
    data = file.readlines()
    quotedNames = data[0].split(",")
    names = re.findall('"([a-zA-Z]+)"', data[0])
names.sort()
allValues = map(getSummedIntVal, enumerate(names))
print(sum(allValues)) # 871198282