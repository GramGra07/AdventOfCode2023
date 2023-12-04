file = open("input.txt", "r")
lines = file.readlines()
file.close()
ovrTotal = 0
for line in lines:
    points = 0
    line = line.replace(line[:8],'')
    winningNums = line.split('|')[0].split(' ')
    currentNums = line.split('|')[1].split(' ')
    wins = []
    for cNum in currentNums:
        currentNums[currentNums.index(cNum)] = currentNums[currentNums.index(cNum)].replace('\n','')
        cNum = cNum.replace('\n','')
        try:
            if not winningNums.index(cNum)==-1:
                if (not cNum == ''):
                    wins.append(cNum)
        except:
            pass
    # print(currentNums)
    wins = list(filter(None, wins))
    if (len(wins)>0):
        print(wins)
        points = 2**(len(wins)-1)
    else:
        points = 0
    print(points)
    ovrTotal += points
print(ovrTotal)

