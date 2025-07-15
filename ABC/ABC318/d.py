import sys
sys.setrecursionlimit(10**8)

def dfs(w):
    global ans
    if all(used):
        ans = max(ans, w)
        return
    u = used.index(False)
    used[u] = True
    for v in range(u+1, n):
        if used[v]:
            continue
        used[v] = True
        dfs(w + D[u][v])
        used[v] = False
    used[u] = False
    

n = int(input())
D = [[0 for i in range(n)] for j in range(n)]
for i in range(n-1):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        D[i][i+j+1] = lst[j]
        D[i+j+1][i] = lst[j]

used = [False for i in range(n)]
ans = 0
if n % 2 == 0:
    dfs(0)
else:
    for i in range(n):
        used[i] = True
        dfs(0)
        used[i] = False
print(ans)