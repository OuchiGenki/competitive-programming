import sys
sys.setrecursionlimit(10**8)

m = int(input())
s1 = list(map(int, list(input())))
s2 = list(map(int, list(input())))
s3 = list(map(int, list(input())))

pos1 = [[] for i in range(10)]
pos2 = [[] for i in range(10)]
pos3 = [[] for i in range(10)]

for i in range(m):
    pos1[s1[i]].append(i)
for i in range(m):
    pos2[s2[i]].append(i)
for i in range(m):
    pos3[s3[i]].append(i)

def is_same(a,b,c):
    if a==b:
        return a
    elif b==c:
        return b
    else:
        return c

ans = 10**18
for num in range(10):
    if len(pos1[num])==0 or len(pos2[num])==0 or len(pos3[num])==0:
        continue

    for a in pos1[num]:
        for b in pos2[num]:
            for c in pos3[num]:
                if a==b==c:
                    res = a+2*m
                elif a==b or b==c or c==a:
                    res = is_same(a,b,c)+m
                else:
                    res = max(a,b,c)
                ans = min(ans, res)

if ans==10**18:
    print(-1)
else:
    print(ans)
    