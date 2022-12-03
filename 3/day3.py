f = open("files/final", "r")

lines = []

for line in f.readlines():
    lines.append(line.strip())

def find_common(list):
    size = len(list) - 1
    count = 0
    for let in list[0]:
        n = size
        while n > 0:
            if let in list[n]:
                count += 1
            n -= 1
        if count == size:
            return let
        count = 0
    raise RuntimeError("Could not find common")

def get_score(slist):
    score = 0

    for letter in slist:
        if letter >= 'A' and letter <= 'Z':
            score += (ord(letter) - 38)
        else:
            score += (ord(letter) - 96)
    return score

def exo1():
    clist = []
    for line in lines:
        clist.append(find_common([line[:len(line)//2], line[len(line)//2:]]))
    return clist


def exo2():
    clist = []
    l = []
    count = 0
    for line in lines:
        l.append(line.strip())
        count += 1
        if count == 3:
            clist.append(find_common(l))
            l = []
            count = 0
    return clist

slist = exo1()
print(f'Exo 1 = {get_score(slist)}')
slist = exo2()
print(f'Exo 2 = {get_score(slist)}')