with open('files/input') as f:
    plays = [(ord(i[0]) - ord('A'), ord(i[2]) - ord('X')) for i in f.read().splitlines()]

r1 = sum([p[1] + 1 + 3 * (p[0] == p[1]) + 6 * ((p[0] + 1) % 3 == p[1]) for p in plays])
print(r1) #12740

r2 = sum([(p[0] + (p[1] - 1)) % 3 + 1 + 3 * p[1] for p in plays])
print(r2) #11980