from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

def dfs(v, now):
    visited[(v, now)] = True
    for weight, next_v in G[v]:
        if visited[(next_v, now^weight)]:
            continue
        dfs(next_v, now^weight)


N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b, w = map(int, input().split())
    G[a-1].append((w, b-1))

visited = defaultdict(bool)
dfs(0, 0)

for i in range(2**10):
    if visited[(N-1, i)]:
        print(i)
        exit()

print(-1)