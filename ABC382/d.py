import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
ans = []

def dfs(A):
    if len(A) == N:
        ans.append(A)
        return

    if len(A)==0:
        left = 1
    else:
        left = A[-1]+10
    right = M-10*(N-len(A)-1)+1

    for i in range(left, right):
        dfs(A+[i])

dfs([])

ans.sort()

print(len(ans))
for i in ans:
    print(*i)
