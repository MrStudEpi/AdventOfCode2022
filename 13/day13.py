#!/usr/bin/env python3

f = open('files/final', 'r')
import ast
from functools import cmp_to_key

lines = []

for line in f:
    lines.append(line.strip())

# Create a parser than can handle this:
# [[1], [2, 3, 4]]
def parseLine(line): # list: int
    return ast.literal_eval(line)
    
def createPairedList():
    list1 = []
    list2 = []
    
    i = 0
    for line in lines:
        if line == "":
            continue
        if i % 2 == 0:
            list1.append(parseLine(line))
        else:
            list2.append(parseLine(line))
        i += 1
    return list1, list2

def compareList(l1, l2):
    i = 0
    while i < len(l1):
        if i >= len(l2):
            return 2
        winner = getWinner(l1[i], l2[i])
        if winner != 0:
            return winner
        i += 1
    if i < len(l2):
        return 1
    return 0

def getWinner(packet_one, packet_two): # 1 = left, 2 = right, 0 = other
    if (type(packet_one) == int and type(packet_two) == int) and packet_one != packet_two:
        return 1 if packet_one < packet_two else 2
    elif (type(packet_one) == list and type(packet_two) == list):
        return compareList(packet_one, packet_two)
    elif (type(packet_one) == list and type(packet_two) == int):
        return compareList(packet_one, [ packet_two ])
    elif (type(packet_one) == int and type(packet_two) == list):
        return compareList([ packet_one ], packet_two)
    return 0

def compare(left, right):
    res = getWinner(left, right)
    
    if res == 1:
        return -1
    elif res == 2:
        return 1
    else:
        return 0

def exo2():
    list1, list2 = createPairedList()
    all = (list1 + list2)
    all.append([[2]])
    all.append([[6]])
    if len(list1) != len(list2):
        print("Error: lists are not of the same length")
        return
    slist = sorted(all, reverse=False, key=cmp_to_key(compare))
    idxs = []
    for i, elem in enumerate(slist):
        if elem == [[2]]:
            idxs.append(i+1)
        elif elem == [[6]]:
            idxs.append(i+1)
    print('Decoder key: ' + str(idxs[0] * idxs[1]))
        
def exo1():
    list1, list2 = createPairedList()
    if len(list1) != len(list2):
        print("Error: lists are not of the same length")
        return
    idxs = []
    for i in range(len(list1)):
        winner = getWinner(list1[i], list2[i])
        if winner == 1:
            idxs.append(i+1)
    print('Sum of idxs: ' + str(sum(idxs)))
 

exo1()
exo2()

f.close()