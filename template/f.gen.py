cases = []
SIZE = 7
for i in range(1,SIZE):
    for j in range(1,SIZE):
        size = i*j
        for a in range(size+1):
            for b in range(size-a+1):
                c = size - a - b
                cases.append((i, j, a, b, c))
strr = str(len(cases))
for case in cases:
    strr += "\n{} {} {} {} {}".format(*case)
with open("f0", "w") as f:
    f.writelines(strr)