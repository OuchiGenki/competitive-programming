import itertools

n, m = map(int, input().split())
s = []
for i in range(m):
    li = list(map(int, input().split()))
    s.append(set(li[1:li[0]+1]))

p = [i for i in range(1, n+1)]

ans = True
for i, j in itertools.combinations(p, 2):
    ok = False
    for k in range(m):
        if i in s[k] and j in s[k]:
            ok = True
    if ok == False:
        ans = False

if ans:
    print("Yes")
else:
    print("No")