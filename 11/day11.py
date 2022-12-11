from functools import reduce

f = open('files/final', 'r')

lines = []

for line in f:
    lines.append(line.strip())
    
    
class Monkey:
    
    monkeyId = 0
    holdingItems = []
    operation = None
    divisableBy = 1
    inspectedTimes = 0
    binds = None
    operationsParameters = None
    
    def __init__(self, monkeyId):
        self.monkeyId = monkeyId
        self.holdingItems = []
        self.operation = None
        self.divisableBy = 1
        self.inspectedTimes = 0
        self.binds = [
            {'condition': True, 'linked_to': 0},
            {'condition': False, 'linked_to': 0},
        ]
        self.operationsParameters = {
            'first': {'defined': False, 'value': 0},
            'second': {'defined': False, 'value': 0},
        }
        
    def addItem(self, item):
        self.holdingItems.append(item)
    
    def setOperation(self, operation): #Lambda
        # Operation is a string with old {factor} {number}
        one, factor, two = operation[0], operation[1], operation[2]
        operationsList = [
            {'factor': '*', 'operation': lambda x, y: x * y},
            {'factor': '+', 'operation': lambda x, y: x + y},
            {'factor': '-', 'operation': lambda x, y: x - y},
            {'factor': '/', 'operation': lambda x, y: x / y},
        ]
        
        try:
            number = int(one)
            self.operationsParameters['first']['defined'] = True
            self.operationsParameters['first']['value'] = number
        except ValueError:
            pass
        
        try:
            number = int(two)
            self.operationsParameters['second']['defined'] = True
            self.operationsParameters['second']['value'] = number
        except ValueError:
            pass
            
        for op in operationsList:
            if op['factor'] == factor:
                self.operation = op['operation']
                return
        
        
    def __str__(self):
        return "Monkey " + str(self.monkeyId) + " holding " + str(self.holdingItems) + " params: " + str(self.operationsParameters)
        
    def setDivisableBy(self, divisableBy):
        self.divisableBy = divisableBy
        
    def doOperation(self, item):
        first = self.operationsParameters['first']['value']
        second = self.operationsParameters['second']['value']
        first = item if self.operationsParameters['first']['defined'] == False else self.operationsParameters['first']['value']
        second = item if self.operationsParameters['second']['defined'] == False else self.operationsParameters['second']['value']
        return self.operation(first, second)
    
    def getBored(self, n):
        return int(n / 3)
    
    def throwItem(self, monkeyList, otherId, item):
        for monkey in monkeyList:
            if monkey.monkeyId == otherId:
                monkey.addItem(item)
                self.holdingItems.pop(0)
                return
        raise("Monkey not found")
    
    def getId(self):
        return self.monkeyId
    
    def doTest(self, monkeyList, n):
        if n % self.divisableBy == 0:
            otherId = self.binds[0]['linked_to']
        else:
            # print(f'\t\tCurrent worry level is not divisible by {self.divisableBy}.')
            otherId = self.binds[1]['linked_to']
        #print(f'\t\tItem with worry level {n} is thrown to monkey {otherId}.')
        self.throwItem(monkeyList, otherId, n)
        return otherId
        
    def setBind(self, condition, otherId):
        for bind in self.binds:
            if bind['condition'] == condition:
                bind['linked_to'] = otherId
                return
        raise("Condition not found")
    
    def getFirstItem(self):
        item = self.holdingItems[0]
        self.holdingItems.pop(0)
        return item
    
    def increaseInspectedTime(self):
        self.inspectedTimes += 1

# Parse this:
# Money {id}:
#   Starting items: {item}, ...
#   Operation: new = {operation}
#   Test: divisible by {divisableBy}
#       If true: throw to monkey {id}
#       If false: throw to monkey {id}
def parseMoney(block):
    # Get id
    block[0] = block[0][:-1]
    monkeyId = int(block[0].split(' ')[1])
    
    # Get items
    items = block[1].split(' ')[2:]
    
    # Get operation
    operation = block[2].split(' ')[3:]
    
    
    # Get divisable by
    divisableBy = int(block[3].split(' ')[3])
    
    # Get binds
    bindTrue = int(block[4].split(' ')[5])
    bindFalse = int(block[5].split(' ')[5])
    # Create monkey
    monkey = Monkey(monkeyId)
    
    # Add items
    for item in items:
        monkey.addItem(int(item.replace(',', '')))
    
    # Set operation
    monkey.setOperation(operation)
    
    # Set divisable by
    monkey.setDivisableBy(divisableBy)
    
    # Set binds
    monkey.setBind(True, bindTrue)
    monkey.setBind(False, bindFalse)
    
    return monkey

def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # Choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def runRound(monkeyList, isBored = True, u = 0):
    for monkey in monkeyList:
        # print(f'Monkey {monkey.getId()}:')
        while len(monkey.holdingItems) > 0:
            item = monkey.holdingItems[0]
            monkey.increaseInspectedTime()
            # print(f'\tMonkey inspects an item with a worry level of {item}.')
            res = monkey.doOperation(item)
            # print(f'\t\tWorry level result is {res}.')
            if isBored:
                res = monkey.getBored(res)
            else:
                # lcm between res and divisableBy
                res = res % u
            # print(f'\t\tMonkey gets bored with item. Worry level is divided by 3 to {res}.')
            monkey.doTest(monkeyList, res)
        # print(f'Monkey holding items: {monkey.holdingItems}')

def findActiveMonkeys(monkeyList, numberOfMonkeys):
    activeMonkeys = []
    for monkey in monkeyList:
        if len(activeMonkeys) < numberOfMonkeys:
            activeMonkeys.append(monkey)
            continue
        for activeMonkey in activeMonkeys:
            if monkey.inspectedTimes > activeMonkey.inspectedTimes:
                activeMonkeys.append(monkey)
                activeMonkeys.sort(key=lambda x: x.inspectedTimes)
                activeMonkeys.pop(0)
                break
    return activeMonkeys

def getMonkeys():
    currentBlock = []
    monkeys = []
    for line in lines:
        if line == "":
            monkeys.append(parseMoney(currentBlock))
            currentBlock = []
            continue
        currentBlock.append(line.strip())
    if currentBlock != []:
        monkeys.append(parseMoney(currentBlock))
    return monkeys

def exo1():
    monkeys = getMonkeys()
    currentRound = 0
    maxRound = 20
    while currentRound != maxRound:
        runRound(monkeys)
        currentRound += 1
    amonkeys = findActiveMonkeys(monkeys, 2)
    total = 1
    for monkey in amonkeys:
        total *= monkey.inspectedTimes
    print(f'Total inspected items: {total}')
    
def exo2():
    monkeys = getMonkeys()
    currentRound = 0
    maxRound = 10000
    divisors = [monkey.divisableBy for monkey in monkeys]
    modulo = reduce(lambda x, y: x*y, divisors)
    while currentRound != maxRound:
        runRound(monkeys, False, modulo)
        currentRound += 1
    amonkeys = findActiveMonkeys(monkeys, 2)
    total = 1
    for monkey in amonkeys:
        total *= monkey.inspectedTimes
    print(f'Total inspected items: {total}')
    
exo1()
exo2()

f.close()