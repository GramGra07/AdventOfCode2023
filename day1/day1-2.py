from colorama import Fore
fileName = "day1-1Input.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line)
file.close()

numbers = ['one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
realNumbers = ['1','2','3','4','5','6','7','8','9']
numbersDict = {'one':'1','two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8','nine':'9'}
calibration_values = []
for line in lines:
    numberLine = ''
    numLength = 0
    numLengthR = 0
    left = 1000000
    right = 0
    for num in realNumbers:
        if num in line:
            if line.find(num) < left:
                left = line.find(num)
                numLength = len(num)
            if line.rfind(num) > right:
                right = line.rfind(num)
                numLengthR = len(num)
    for num in numbers:
        if num in line:
            if line.find(num) < left:
                left = line.find(num)
                numLength = len(num)
            if line.rfind(num) > right:
                right = line.rfind(num)
                numLengthR = len(num)

    if (not line[left:left+numLength] in realNumbers):
        numberLine += str(numbersDict.get(line[left:left+numLength]))
    else:
        numberLine += line[left:left+1]
    if not line[right:right + numLengthR] in realNumbers:
        numberLine += str(numbersDict.get(line[right:right+numLengthR]))
    else:
        numberLine += line[right:right+1]
    print(line[:left] + Fore.GREEN + line[left:left+numLength] + Fore.RED + line[left+numLength:right] + Fore.GREEN + line[right:right+numLengthR] + Fore.RED + line[right+numLengthR:])

    # if (not numberLine == 'None'):
    if (len(numberLine)!=2):
        if ('None' in numberLine):
            numberLine = numberLine.replace('None','')
        numberLine*=2
    if (len(numberLine)==2):
        # print(numberLine)
        calibration_values.append(int(numberLine))
# print(calibration_values)
total = sum(calibration_values)
print(Fore.RESET)
print(total)