import sys
sys.setrecursionlimit(10**7)

n = int(input())
d = {}

for i in range(n):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = []
    d[a].append(b)
    if b not in d:
        d[b] = []
    d[b].append(a)

seen = set()
ans = 1

def dfs(x):
    global ans
    ans = max(ans, x)
    seen.add(x)
    if x not in d: return
    for nx in d[x]:
        if nx in seen:
            continue
        dfs(nx)

dfs(1)

print(ans)