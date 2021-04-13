#Can be improved by reusing previously generated strings. Like for the 40 in 540 and so on.

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
specialTens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def getLetterCount(number):
    wordString = ""
    #used to figure out whether "and" is to be appended
    usesTens = False
    numberString = str(number)[::-1]
    #used for the ten's place when we need unit's place info as well(11,12,etc.)
    previousNumChar = 0
    for index, numChar in enumerate(numberString):
        if index == 0 and int(numChar) > 0:
            wordString = wordString+ones[int(numChar)-1]
            usesTens = True
        if index == 1 and int(numChar) == 1:
            wordString = ""
            wordString = wordString+specialTens[int(previousNumChar)]
            usesTens = True
        elif index == 1 and int(numChar) > 1:
            wordString = wordString+tens[int(numChar)-2]
            usesTens = True
        if index == 2 and int(numChar) > 0:
            wordString = wordString+ones[int(numChar)-1]+"hundred"
            if usesTens:
                wordString = wordString+"and"
        if index == 3 and int(numChar) > 0:
            wordString = wordString+ones[int(numChar)-1]+"thousand"
        previousNumChar = numChar   
    return len(wordString)

endIndex = 1001
totalCount = 0

for index in range(1, endIndex):
    totalCount = totalCount + getLetterCount(index)
print(totalCount)
