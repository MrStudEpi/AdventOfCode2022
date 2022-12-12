#!/usr/bin/env python3

from copy import deepcopy
from queue import Queue

f = open('files/final', 'r')

lines = []

for line in f:
    lines.append(line.strip())

DAY = 12


def isValid(matrix, i, j):
    return not(i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]))

def canReach(matrix, i_next, j_next, i, j, distance, mod = 0):
    if mod == 0:
        return ord(matrix[i_next][j_next])-ord(matrix[i][j]) <= 1 and distance[i_next][j_next] < 1
    else:
        return ord(matrix[i][j])-ord(matrix[i_next][j_next]) <= 1 and distance[i_next][j_next] < 1

def initDistance(matrix, start):
    distance = [[0 for _ in range(len(matrix[j]))] for j in range(len(matrix))]
    distance[start[0]][start[1]] = 1
    return distance

def lee(matrix, start, end):
    distance = initDistance(matrix, start)

    matrix[start[0]][start[1]] = 'a'
    matrix[end[0]][end[1]] = 'z'
    
    Q = Queue()
    Q.put(start)
    
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while not Q.empty():
        i, j = Q.get()

        for k in range(4):
            i_next, j_next = i + d[k][0], j + d[k][1]
            
            if isValid(matrix, i_next, j_next) and canReach(matrix, i_next, j_next, i, j, distance):
                distance[i_next][j_next] = distance[i][j] + 1

                Q.put((i_next, j_next))

    return distance[end[0]][end[1]]-1


def reverse_lee(matrix, start, end):
    distance = initDistance(matrix, start)

    matrix[start[0]][start[1]] = 'z'
    
    Q = Queue()
    Q.put(start)
    
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    possible = []
    while not Q.empty():
        i, j = Q.get()

        for k in range(4):
            i_next, j_next = i + d[k][0], j + d[k][1]
            
            if isValid(matrix, i_next, j_next) and canReach(matrix, i_next, j_next, i, j, distance, 1):
                distance[i_next][j_next] = distance[i][j] + 1
                
                if matrix[i_next][j_next] == end:
                    possible.append(distance[i][j])
                
                Q.put((i_next, j_next))
    
    return min(possible)

def findSymbol(sym):
    for i, y in enumerate(lines):
        idx = y.find(sym)
        if idx != -1:
            return (i, idx)
    return (0, 0)

def exo1():
    matrix = []
    
    for line in lines:
        matrix.append(list(line))
    start = findSymbol('S')
    end = findSymbol('E')
    
    return lee(matrix, start, end)


def exo2():
    matrix = []
    for line in lines:
        matrix.append(list(line))
    start = findSymbol('E')
    
    return reverse_lee(matrix, start, 'a')

print(f"Part 1: {exo1()}")
print(f"Part 2: {exo2()}")