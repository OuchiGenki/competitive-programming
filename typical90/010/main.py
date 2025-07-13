n = int(input())
p1 = []
p2 = []
for i in range(n):
    C, P = map(int, input().split())
    if C == 1:
        p1.append(P)
        p2.append(0)
    else:
        p1.append(0)
        p2.append(P)

sumP1 = [0]
sumP2 = [0]

for i in range(n):
    sumP1.append(sumP1[i] + p1[i])
    sumP2.append(sumP2[i] + p2[i])

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(sumP1[r]-sumP1[l-1], sumP2[r]-sumP2[l-1])