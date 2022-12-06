f = open("files/final", "r")

lines = []

for line in f.readlines():
    lines.append(line)
    
def exo1():
    for line in lines:
        idx = 0
        for i in range(0, len(line)):
            l = []
            for j in range(i, i + 4):
                if line[j] in l:
                    break
                l.append(line[j])
                idx = j + 1
            if len(l) == 4:
                break
        print(idx)
        
def exo2():
    for line in lines:
        idx = 0
        for i in range(0, len(line)):
            l = []
            for j in range(i, i + 14):
                if line[j] in l:
                    break
                l.append(line[j])
                idx = j + 1
            if len(l) == 14:
                break
        print(idx)

exo1()
exo2()