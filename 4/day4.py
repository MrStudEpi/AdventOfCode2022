f = open("files/final", "r")

lines = []

for line in f.readlines():
    lines.append(line.strip())

def exo1():
    count = 0

    for line in lines:
        elems = line.split(',')
        nums = elems[0].split('-')
        min = int(nums[0])
        max = int(nums[1])
        nums = elems[1].split('-')
        n1 = int(nums[0])
        n2 = int(nums[1])
        if n1 >= min and n2 <= max:
            count += 1
        elif min >= n1 and max <= n2:
            count += 1
    print(count)

def exo2():
    count = 0

    for line in lines:
        elems = line.split(',')
        nums = elems[0].split('-')
        min = int(nums[0])
        max = int(nums[1])
        nums = elems[1].split('-')
        n1 = int(nums[0])
        n2 = int(nums[1])
        range1 = range(n1, n2+1)
        range2 = range(min, max+1)

        z = [i for i in range1 if i in range2]
        if z != []:
            count += 1

    print(count)


exo1()
exo2()