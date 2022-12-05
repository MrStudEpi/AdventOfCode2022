import re

f = open("files/final", "r")

lines = []

for line in f.readlines():
    lines.append(line)

final = []

# Parse that
#
#    [D]    
# [N] [C]    
# [Z] [M] [P]
# 1   2   3 "

# Create a stack for each pos in final
def setup_stack(liste):
    # find max pos in final
    maxi = 0
    for i in liste:
        if i['pos'] > maxi:
            maxi = i['pos']
    # create a stack for each pos
    stack = []
    for i in range(0, maxi+1):
        stack.append([])
    # fill the stack
    for i in liste:
        stack[i['pos']].append(i['element'])
    return stack

def move(line, stack):
    nums = re.findall(r'\d+', line)
    
    number = int(nums[0])
    frome = int(nums[1])-1
    to = int(nums[2])-1

    for i in range(0, number):
        stack[to] = [stack[frome][0]] + stack[to]
        stack[frome].pop(0)

def exo1():
    i = 0
    stack = []
    for line in lines:
        if line == "\n" or line[1].isdigit():
            continue
        if line.startswith("move"):
            if stack == []:
                stack = setup_stack(final)
            move(line, stack)
        else:
            c = 0
            for i in range(0, len(line), 4):
                if i > len(line):
                    break
                if line[i] != " ":
                    final.append({'pos': c, 'element': line[i:i+3]})
                c += 1
    for s in stack:
        print(s[0], end=" ")
        
def move2(line, stack):
    nums = re.findall(r'\d+', line)
    
    number = int(nums[0])
    frome = int(nums[1])-1
    to = int(nums[2])-1

    r = []
    for i in range(0, number):
        r = r + [stack[frome][0]]
        stack[frome].pop(0)
    stack[to] = r + stack[to]
    
def exo2():
    i = 0
    stack = []
    for line in lines:
        if line == "\n" or line[1].isdigit():
            continue
        if line.startswith("move"):
            if stack == []:
                stack = setup_stack(final)
            move2(line, stack)
        else:
            c = 0
            for i in range(0, len(line), 4):
                if i > len(line):
                    break
                if line[i] != " ":
                    final.append({'pos': c, 'element': line[i:i+3]})
                c += 1
    for s in stack:
        print(s[0], end=" ")
    
exo1()
print('')
exo2()