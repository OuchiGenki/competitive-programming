import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
g = [[] for i in range(n)]
seen = [False for i in range(n)]
ans = 0

for i in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def dfs(tg, seen):
    seen[tg] = True
    global ans
    ans += 1
    
    for next_tg in g[tg]:
        if seen[next_tg]: continue
        if ans == 10**6: return
        dfs(next_tg, seen)
    seen[tg] = False

dfs(0, seen)
print(ans)