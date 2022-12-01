f = open("files/input", "r")

elfs = []
elf_number = 0

for line in f.readlines():
    if line == "\n":
        elf_number += 1
    else:
        if len(elfs) <= elf_number:
            elfs.append([])
        elfs[elf_number].append(int(line))

maxed = []

def getMaximum(elfs_list):
    maximum = 0
    index = 0
    for i, elf in enumerate(elfs_list):
        total = 0
        for score in elf:
            total += score
        if total > maximum:
            maximum = total
            index = i
    return maximum, index

result = 0

for i in range(3):
    max, index = getMaximum(elfs)
    result += max
    del elfs[index]

print(result)