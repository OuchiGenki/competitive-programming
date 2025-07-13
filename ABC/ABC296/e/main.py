import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(v):
    global cnt
    seen[v] = True
    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)
    num[cnt] = v
    cnt += 1

def rdfs(v):
    global cnt
    cnt += 1
    seen[v] = True
    for nv in rg[v]:
        if seen[nv]:
            continue
        roop.add(nv)
        rdfs(nv)

n = int(input())
a = list(map(int, input().split()))

g = [[] for i in range(n)]
rg = [[] for i in range(n)]
roop = set()
for i in range(n):
    if i+1 == a[i]:
        roop.add(i)
    else:
        g[i].append(a[i]-1)
        rg[a[i]-1].append(i)

seen = [False for i in range(n)]
num = [0 for i in range(n)]
cnt = 0
for i in range(n):
    if seen[i]:
        continue
    dfs(i)

seen = [False for i in range(n)]
for i in range(n-1, -1, -1):
    v = num[i]
    cnt = 0
    if seen[v]:
        continue
    rdfs(v)
    if cnt > 1:
        roop.add(v)

ans = set()
for i in range(n):
    if i in roop:
        ans.add(a[i])

print(len(ans))