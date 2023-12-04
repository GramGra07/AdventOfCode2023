file = open("input.txt", "r")
lines = file.readlines()
file.close()
instances = [1 for _ in lines]  # 1 for each line and index
for index, line in enumerate(lines):  # 0, "~~~~~~"
    line = line.split(":")[1]  # only keep right side of colon
    a, b = line.split("|")  # split into two parts, a and b keep both
    a, b = a.split(), b.split()  # split into individual numbers

    n = len(set(a) & set(b))  # number of common elements

    for i in range(n):  # for each common element
        instances[index + i + 1] += instances[index]  # add to next index

print(sum(instances))
