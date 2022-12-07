f = open("files/final", "r")

lines = []

for line in f:
    lines.append(line)

class Component:
    # name: string
    # size: int
    # type: 0 = file, 1 = directory
    # children: list of Component
    # parent: Component
    def __init__(self, name, size, type, children, parent):
        self.name = name
        self.size = size
        self.children = children
        self.type = type
        self.parent = parent
        
    def addDirectory(self, name):
        self.children.append(Component(name, 0, 1, [], self))
        
    def addFile(self, name, size):
        self.size += size
        parent = self.parent
        while parent != None:
            parent.size += size
            parent = parent.parent
        self.children.append(Component(name, size, 0, [], self))
        
    def goUp(self):
        return self.parent
    
    def goRoot(self):
        actualDir = self
        while actualDir.parent != None:
            actualDir = actualDir.parent
        return actualDir
    
    # Example of path: /home/alex
    def goTo(self, path):
        # Init actualDir
        actualDir = self
        # If path is empty, return actualDir
        if path == "" or path == ".":
            return actualDir
        if path == "..":
            return self.goUp()
        if path == "/":
            return self.goRoot()
        # If path start with /, go to root
        if path[0] == "/":
            actualDir = self.goRoot()
            path = path[1:]
        # Go to the next directory
        goDir = path[:path.find("/")] if path.find("/") != -1 else path
        for child in actualDir.children:
            if child.name == goDir:
                actualDir = child
                return actualDir.goTo(path[len(goDir):])
        return None

def cd(actualDir, path):
    return actualDir.goTo(path)

def printComponent(component, level = 0):
    print(" " * level + "- " + component.name + " (" + ("file" if component.type == 0 else "dir") + ", size=" + str(component.size) + ")")
    for child in component.children:
        printComponent(child, level + 1)
        
# Function that take a component filter by size and directory type
# take only directory with size > 100000 and add their size to total
def filterSize(component, total):
    if component.type == 1:
        if component.size <= 100000:
            total += component.size
        for child in component.children:
            total = filterSize(child, total)
    return total

def exo1():
    dire = Component("/", 0, 1, [], None)
    global root
    root = dire
    
    for line in lines:
        elems = line.strip().split(" ")
        if elems[0] == "$":
            elems.pop(0)
        command = elems[0]
        if line[0] == "$":
            if command == "cd":
                dire = cd(dire, elems[1])
            elif command == "ls":
                pass
            else:
                print("Command not found")
        else:
            data = elems[1]
            if command == "dir":
                dire.addDirectory(data)
            else:
                dire.addFile(data, int(command))
    # print root Component
    printComponent(root)
    print(filterSize(root, 0))

def findSmallestDir(component, emptyDisk, neededDisk):
    
    if (emptyDisk + component.size) < neededDisk:
        return None
    smallestDif = component.size
    smallestDir = component
    for child in component.children:
        if child.type == 0:
            continue
        res = findSmallestDir(child, emptyDisk, neededDisk)
        if res == None:
            continue
        diff = emptyDisk + res.size - neededDisk
        if diff < smallestDif:
            smallestDif = diff
            smallestDir = res
    return smallestDir

def exo2():
    totalDisk = 70000000
    neededDisk = 30000000
    emptyDisk = totalDisk - root.size
    
    # Find the smallest directory that is superior to emptyDisk
    res = findSmallestDir(root, emptyDisk, neededDisk)
    print("Smallest directory:", res.size)
            
exo1()
exo2()
    
f.close()