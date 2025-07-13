from itertools import permutations

def check():
    xy = [[a, b] for a, b in enumerate(p)]
    if len(set([a+b for a,b in xy])) != 8 or len(set([a-b for a,b in xy])) != 8:
        return False
    else:
        return True


k = int(input())
rc = []
for i in range(k):
    r, c = map(int, input().split())
    rc.append((r, c))
li = [i for i in range(8)]

g = [['.' for i in range(8)] for j in range(8)]

for p in permutations(li):
    skip = False
    for r, c in rc:
        if p[r] != c:
            skip = True
            break
    if skip:
        continue        
    if check():
        for y,x in enumerate(p):
            g[y][x] = 'Q'

for i in g:
    print(*i, sep="")