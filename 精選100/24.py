import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    global cnt
    seen[v] = True
    ans[v][1] = cnt
    for nv in g[v]:
        if seen[nv]:
            continue
        cnt += 1
        dfs(nv)
    cnt += 1
    ans[v][2] = cnt

n = int(input())
g = [[] for i in range(n)]
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(len(li)):
        if j >= 2:
            g[i].append(li[j]-1)

ans = [[j+1 for i in range(3)] for j in range(n)]
seen = [False for i in range(n)]
cnt = 1
for i in range(n):
    if seen[i] == False:
        dfs(i)
        cnt += 1


for i in ans:
    print(*i)