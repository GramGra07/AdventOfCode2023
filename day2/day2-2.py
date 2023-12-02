file = open("input.txt", "r")
lines = file.readlines()
file.close()
total = 0
maxes = []
rgb = ['red', 'green', 'blue']
for line in lines:
    lineNumber = lines.index(line)+1
    redGreenBlue = []
    rMax = 0
    gMax = 0
    bMax = 0
    ogLine = line
    line = line.replace('Game:', '')
    line = line.replace('\n', '')
    line = line[line.find(':') + 1:]
    game = (line.split(';'))
    for set in game:
        set2 = set.split(',')
        for i in range(len(set2)):
            set2[i] = set2[i].replace(' ', '')
            if ('red' in set2[i]):
                set2[i] = set2[i].replace('red', '')
                if int(set2[i])>rMax:
                    rMax = int(set2[i])
            if ('green' in set2[i]):
                set2[i] = set2[i].replace('green', '')
                if (int(set2[i])>gMax):
                    gMax = int(set2[i])
            if ('blue' in set2[i]):
                set2[i] = set2[i].replace('blue', '')
                if (int(set2[i])>bMax):
                    bMax = int(set2[i])
    maxes.append(rMax*gMax*bMax)
    total = sum(maxes)
print(total)
