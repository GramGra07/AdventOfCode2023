file = open("test.txt", "r")
lines = file.readlines()
file.close()
ovrTotal = 0
cards = {}
total = 0
points = 0
copies = {}
for line in lines:
    ogLine = line
    line = line.replace(line[:4],'')
    number = line[:3]
    line = line.replace(line[:3],'')
    winningNums = line.split('|')[0].split(' ')
    currentNums = line.split('|')[1].split(' ')

    for cNum in currentNums:
        currentNums[currentNums.index(cNum)] = currentNums[currentNums.index(cNum)].replace('\n','')
        cNum = cNum.replace('\n','')
    cards[lines.index(ogLine)+1] = [winningNums,currentNums]

    for card in cards:
        wins = []
        winningNums = cards[card][0]
        for cNum in cards[card][1]:
            try:
                if not cards[card][0].index(cNum)==-1:
                    if (not cNum == ''):
                        wins.append(cNum)
            except:
                pass
        wins = list(filter(None, wins))
        # add the next len(wins) to copies
        num = number.replace(':','')
        num = num.replace(' ','')
        num = int(num)
        copies[num] = [len(wins)]
    # wins have been gotten

    for copy in copies:
        print(copy)
print(points)