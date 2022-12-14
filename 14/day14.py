#!/usr/bin/env python3

f = open("files/final", "r")

lines = []

for line in f:
    lines.append(line.strip())
    
def getPrerequisites():
    min, max = 100000, -100000
    max1 = -100000
    pCollection = []
    
    for line in lines:
        elems = line.split("->")

        dict = []
        for elem in elems:
            nums = elem.strip().split(",")
            f, s = int(nums[0]), int(nums[1])
            if f < min:
                min = f
            elif f > max:
                max = f
            if s > max1:
                max1 = s
            dict.append((f, s))
        pCollection.append(dict)
    return pCollection, (min, max), max1

def createMatrix(nb_cols, nb_rows):
    matrix = []
    for row in range(nb_rows):
        matrix.append([0] * nb_cols)
        for col in range(nb_cols):
            matrix[row][col] = '.'
    return matrix

def drawLine(matrix, x1, y1, x2, y2):
    if x1 == x2:
        yMin = min(y1, y2)
        yMax = max(y1, y2)
        for y in range(yMin, yMax + 1):
            matrix[y][x1] = '#'
    elif y1 == y2:
        xMin = min(x1, x2)
        xMax = max(x1, x2)
        for x in range(xMin, xMax + 1):
            matrix[y1][x] = '#'
    else:
        print("Error: not a line", x1, y1, x2, y2)
    return matrix

def fillMatrix(matrix, min, pCollection):
    for keys in pCollection:
        for i in range(len(keys) - 1):
            key1 = keys[i]
            key2 = keys[i + 1]
            matrix = drawLine(matrix, key1[0] - min, key1[1], key2[0] - min, key2[1])
    return matrix

def isNextAvailable(matrix, next_pos):
    if (next_pos[0] >= 0 and next_pos[0] < len(matrix)) and matrix[next_pos[0]][next_pos[1]] == '.':
        return True
    return False

def isInBounds(matrix, pos):
    if (pos[0] >= 0 and pos[0] < len(matrix)) and (pos[1] >= 0 and pos[1] < len(matrix[0])):
        return True
    return False

def getNextPosition(matrix, obs_pos):
    left_pos = (obs_pos[0], obs_pos[1] - 1)
    right_pos = (obs_pos[0], obs_pos[1] + 1)
    pos = obs_pos
    
    if isInBounds(matrix, left_pos) and matrix[left_pos[0]][left_pos[1]] == '.':
        pos = left_pos
    elif isInBounds(matrix, right_pos) and matrix[right_pos[0]][right_pos[1]] == '.': 
        pos = right_pos
    # if pos is out of bounds
    if pos == obs_pos and not isInBounds(matrix, left_pos) or not isInBounds(matrix, right_pos):
        return None
    if pos != obs_pos and not isNextAvailable(matrix, pos):
        pos = getNextPosition(matrix, pos)
    return pos

def simulate(matrix, gPos):
    path = []
    
    curr_pos = gPos
    next_pos = None
    while curr_pos[0] < len(matrix):
        next_pos = (curr_pos[0] + 1, curr_pos[1])
        path.append(curr_pos)
        if not isNextAvailable(matrix, next_pos):
            next_pos = getNextPosition(matrix, next_pos)
        if next_pos == None:
            return path, None
        if matrix[next_pos[0]][next_pos[1]] != '.':
            return path, curr_pos
        curr_pos = next_pos
    return path, None

def exo1():
    pCollection, col_bounds, max_row = getPrerequisites()
    matrix = createMatrix(col_bounds[1] - col_bounds[0] + 1, max_row + 1)
    matrix = fillMatrix(matrix, col_bounds[0], pCollection)
    gPos = (0, 500 - col_bounds[0])
    matrix[gPos[0]][gPos[1]] = '+'
    count = 0
    while True:
        path, res = simulate(matrix, gPos)
        if res == None:
            break
        matrix[res[0]][res[1]] = 'o'
        count += 1
    return count
    
def exo2():
    pCollection, col_bounds, max_row = getPrerequisites()
    offset = 400
    col_bounds = (col_bounds[0] - offset, col_bounds[1] + offset)
    max_row += 2
    pCollection.append([(col_bounds[0], max_row), (col_bounds[1], max_row)])
    matrix = createMatrix(col_bounds[1] - col_bounds[0] + 1, max_row + 1)
    matrix = fillMatrix(matrix, col_bounds[0], pCollection)
    gPos = (0, 500 - col_bounds[0])
    matrix[gPos[0]][gPos[1]] = '+'
    count = 0
    while True:
        path, res = simulate(matrix, gPos)
        if res == None or res == gPos:
            break
        matrix[res[0]][res[1]] = 'o'
        count += 1
    return count + 1

count = exo1()
print('Exercice 1: ' + str(count))
count = exo2()
print('Exercice 2: ' + str(count))
    
f.close()