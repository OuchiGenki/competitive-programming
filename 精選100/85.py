k = int(input())

n = set()
for a in range(1, 10**4+1):
    if k%a == 0:
        n.add(a)
        n.add(k//a)


