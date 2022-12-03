f = open("files/final", "r")

rucksacks = []
l = []
count = 0

clist = []

def find_common(list):
    for i in range(len(list)):
        for let in list[0]:
            if let in list[1] and let in list[2]:
                return let

for line in f.readlines():
    n = len(line)
    print(line)
    l.append(line.strip())
    count += 1
    if count == 3:
        clist.append(find_common(l))
        l = []
        count = 0

score = 0

for letter in clist:
    if letter >= 'A' and letter <= 'Z':
        score += (ord(letter) - 38)
    else:
        score += (ord(letter) - 96)

print(score)