import sys
sys.setrecursionlimit(10**6)

def dfs(v, c):
    visited[v] = True
    X[v] = c
    flag = True

    for nv in G[v]:
        if X[nv] == c:
            flag = False
            break
        if visited[nv]:
            continue
        flag = dfs(nv, (c+1)%2)
    
    return flag

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
G = [[] for _ in range(N)]
for i in range(M):
    G[A[i]-1].append(B[i]-1)
    G[B[i]-1].append(A[i]-1)

visited = [False for i in range(N)]
X = [-1 for i in range(N)]

for i in range(N):
    if visited[i]:
        continue
    if not dfs(i, 0):
        print('No')
        exit()

print('Yes')