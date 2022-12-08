f = open("files/final", "r")

lines = []

for line in f:
    lines.append(line)

height = len(lines)
width = len(lines[0]) - 1

coords = []

def isOK(x, y, dx, dy, elem):
    nx = x + dx
    ny = y + dy
    while 1:
        if nx == 0 or nx == (width - 1) or ny == 0 or ny == (height - 1):
            return elem > int(lines[ny][nx])
        if int(lines[ny][nx]) >= elem:
            return 0
        nx += dx
        ny += dy


def isVisible(x, y):
    elem = int(lines[y][x])
    if x == 0 or x == (width - 1) or y == 0 or y == (height - 1):
        return 1
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 and dx != 0:
                continue
            if dy == 0 and dx == 0:
                continue
            if isOK(x, y, dx, dy, elem):
                return 1
    return 0

def exo1():
    count = 0
    for i in range(height):
        for j in range(width):
            if isVisible(j, i):
                count += 1
            
    print(count)
    
def getScoreDir(x, y, dx, dy, elem):
    nx = x + dx
    ny = y + dy
    count = 1
    while 1:
        if nx == 0 or nx == (width - 1) or ny == 0 or ny == (height - 1):
            return count
        if int(lines[ny][nx]) >= elem:
            return count
        nx += dx
        ny += dy
        count += 1
    
    
def getScore(x, y):
    if x == 0 or x == (width - 1) or y == 0 or y == (height - 1):
        return 0
    elem = int(lines[y][x])
    score = 1
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 and dx != 0:
                continue
            if dy == 0 and dx == 0:
                continue
            score *= getScoreDir(x, y, dx, dy, elem)
    return score
    
    
def exo2():
    count = 0
    bestScore = 0
    bestPos = (0, 0)
    for i in range(height):
        for j in range(width):
            score = getScore(j, i)
            if score > bestScore:
                bestScore = score
                bestPos = (j, i)
    print(bestScore, bestPos)
    
exo1()
exo2()

f.close()