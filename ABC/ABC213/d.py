from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10**8)

def dfs(v):
    visited[v] = True
    ans.append(v+1)
    for nv in to[v]:
        if visited[nv]:
            continue
        dfs(nv)
        ans.append(v+1)
    if v+1 == 1:
        return
       

n = int(input())
to = [SortedList() for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    to[a-1].add(b-1)
    to[b-1].add(a-1)
visited = [False] * n
ans = []
dfs(0)

print(*ans)