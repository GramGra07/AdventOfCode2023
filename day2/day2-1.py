file = open("input.txt", "r")
lines = file.readlines()
file.close()
rMax = 12
gMax = 13
bMax = 14
possible = 0
rgb = ['red', 'green', 'blue']
for line in lines:
    lineNumber = lines.index(line)+1
    redGreenBlue = []
    ogLine = line
    line = line.replace('Game:', '')
    line = line.replace('\n', '')
    line = line[line.find(':') + 1:]
    game = (line.split(';'))
    isPossible = True
    for set in game:
        set2 = set.split(',')
        for i in range(len(set2)):
            set2[i] = set2[i].replace(' ', '')
            if ('red' in set2[i]):
                set2[i] = set2[i].replace('red', '')
                if int(set2[i])>rMax:
                    isPossible = False
                    break
            if ('green' in set2[i]):
                set2[i] = set2[i].replace('green', '')
                if (int(set2[i])>gMax):
                    isPossible = False
                    break
            if ('blue' in set2[i]):
                set2[i] = set2[i].replace('blue', '')
                if (int(set2[i])>bMax):
                    isPossible = False
                    break
    if isPossible:
        possible += lineNumber
print(possible)
