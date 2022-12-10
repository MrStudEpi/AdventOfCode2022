f = open('files/final', 'r')

lines = []

for line in f:
    lines.append(line)

# List of instructions and number of cycles to execute
instructions = [
    {'name': "noop", 'cycle': 1},
    {'name': "addx", 'cycle': 2},
]

def findInstruction(instruction):
    for i in instructions:
        if i['name'] == instruction:
            return i
    return None

def initInstructions():
    totalCycle = 0
    instructions = []
    for line in lines:
        elements = line.strip().split()
        # Find in instructions if elements[0] exists
        ex = findInstruction(elements[0])
        num = int(elements[1]) if len(elements) >= 2 else 0
        if ex is not None:
            instructions.append(dict({'name': ex['name'], 'cycle': ex['cycle'], 'number': num}))
            totalCycle += ex['cycle']
        else:
            raise("Unknown instruction")
    return (totalCycle, instructions)

def getInstructionAtCycle(instructions, cycle):
    currentCycle = 0
    for i in instructions:
        currentCycle += i['cycle']
        if currentCycle > cycle:
            return i
    return None

def exo2():
    totalCycle, instructions = initInstructions()
    fmap = []
    crt = []
    cycle = 0
    tmp = 0
    x = 1
    lastInstruction = None
    while cycle != totalCycle:
        ex = getInstructionAtCycle(instructions, cycle)
        if tmp != 0 and tmp % 40 == 0:
            fmap.append(''.join(crt))
            crt = []
            tmp = 0
        if lastInstruction is None:
            lastInstruction = ex
        elif lastInstruction is not ex:
            x += lastInstruction['number']
            lastInstruction = ex
        crt.append('#' if (tmp + 1) >= x and (tmp + 1) < x + 3 else '.')
        tmp += 1
        cycle += 1
    fmap.append(''.join(crt))
    for i in fmap:
        print (i)
    return 0
    
def exo1():
    totalCycle, instructions = initInstructions()
    cycle = 0
    x = 1
    lastInstruction = None
    listCycles = [
        20,
        60,
        100,
        140,
        180,
        220,
    ]
    total = 0
    while cycle != totalCycle:
        ex = getInstructionAtCycle(instructions, cycle)
        if cycle in listCycles:
            total += (cycle * x)
        if lastInstruction is None:
            lastInstruction = ex
        elif lastInstruction is not ex:
            x += lastInstruction['number']
            lastInstruction = ex
        cycle += 1
    return total
        
x = exo1()
print("Exo 1 : " + str(x))
x = exo2()
print("Exo 2 : " + str(x))

f.close()