import re

file = open("input.txt", "r")
lines = file.readlines()
file.close()
total = 0
rows = lines
symbols = ["*"]
killsymbols = ["#", "&", "@", "!", "$", "%", "-", "+", "=",
           "/"]
realNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
rowsArray = []
ogArray = []
for row in rows:
    # create 2D array from lines
    row = row.replace("\n", "")
    rowsArray.append((row))
    ogArray.append((row))
for row in rowsArray:
    ogLine = row
    pattern = re.compile(r'\b\d+\b')  # Matches whole numbers
    iter_matches = pattern.finditer(row)
    for match in iter_matches:
        end = match.end()
        start = match.start()
        row = row.replace('\n', '')
        # make sure no spots adjacent to the current spot are in the symbols array
        if (end == len(row)):
            end -= 1
        if ((row[match.start() - 1] not in symbols) and (
                rowsArray[ogArray.index(ogLine) - 1][match.start() + 1] not in symbols) and (
                rowsArray[ogArray.index(ogLine) - 1][end - 1] not in symbols) and (
                        row[end] not in symbols) and (
                rowsArray[ogArray.index(ogLine) - 1][end] not in symbols) and (
                rowsArray[ogArray.index(ogLine) - 1][match.start()] not in symbols) and (
                rowsArray[ogArray.index(ogLine) - 1][match.start() - 1] not in symbols)):
            if ogArray.index(ogLine) != len(rowsArray) - 1:
                if (rowsArray[ogArray.index(ogLine) + 1][end] not in symbols) and (
                        rowsArray[ogArray.index(ogLine) + 1][match.end() - 1] not in symbols) and (
                        rowsArray[ogArray.index(ogLine) + 1][match.start() + 1] not in symbols) and (
                        rowsArray[ogArray.index(ogLine) + 1][match.start()] not in symbols) and (
                        rowsArray[ogArray.index(ogLine) + 1][match.start() - 1] not in symbols):
                    # row = row[match.start():match.end()].replace(match.group(), "H" * len(match.group()))
                    for i in range(match.start(), match.end()):
                        row = row[:i] + "." + row[i + 1:]
                    rowsArray[ogArray.index(ogLine)] = row
            else:
                row = row.replace(match.group(), "." * len(match.group()))
                rowsArray[ogArray.index(ogLine)] = row
    # print(row)
    # print(match.start(), match.end(), match.group())
for row in rowsArray:
    ogArray = rowsArray
    ogLine = row
    pattern = re.compile(r'\b\d+\b')  # Matches whole numbers
    iter_matches = pattern.finditer(row)
    for s in killsymbols:
        row = row.replace(s, '.')
    for i in range(row.count('*')):
        numbers = []
        count = 0
        ran=3
        num = row.find('*')
        if (rowsArray[ogArray.index(ogLine)][num+1] in realNumbers):
            r = rowsArray[ogArray.index(ogLine)][num-3:num+3]
            r = r.split('.')
            for i in r:
                if not i == '':
                    numbers.append(i)
        if (rowsArray[ogArray.index(ogLine)][num-1] in realNumbers):
            r = rowsArray[ogArray.index(ogLine)][num-3:num+3]
            r = r.split('.')
            for i in r:
                if not i == '':
                    numbers.append(i)
        if (not ogArray.index(ogLine) == 0):
            if (rowsArray[ogArray.index(ogLine) - 1][num + 1] in realNumbers):
                r = rowsArray[ogArray.index(ogLine) - 1][num - ran:num + ran]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
            if (rowsArray[ogArray.index(ogLine)-1][num] in realNumbers):
                r = rowsArray[ogArray.index(ogLine) - 1][num-3:num+3]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
            if (rowsArray[ogArray.index(ogLine)-1][num-1] in realNumbers):
                r = rowsArray[ogArray.index(ogLine)-1][num-ran:num+ran]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
        if (not ogArray.index(ogLine) == len(rowsArray)-1):
            if (rowsArray[ogArray.index(ogLine) + 1][num] in realNumbers):
                r = rowsArray[ogArray.index(ogLine) + 1][num - ran:num + ran]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
            if (rowsArray[ogArray.index(ogLine)+1][num+1] in realNumbers):
                r = rowsArray[ogArray.index(ogLine)+1][num-ran:num+ran]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
            if (rowsArray[ogArray.index(ogLine)+1][num-1] in realNumbers):
                r = rowsArray[ogArray.index(ogLine)+1][num-ran:num+ran]
                r = r.split('.')
                for i in r:
                    if not i == '':
                        numbers.append(i)
        for n in numbers:
            numbers[numbers.index(n)] = numbers[numbers.index(n)].replace('*', '')
        numbers = list(set(numbers))
        print(numbers)
        if len(numbers)==2:
            gr = int(numbers[0]) * int(numbers[1])
            print('gr', gr)
            total+= int(numbers[0]) * int(numbers[1])
            row = row.replace('*', 'Q')
    print(row)
print(total)
#76504829
