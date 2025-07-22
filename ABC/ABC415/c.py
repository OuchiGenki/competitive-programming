import sys
sys.setrecursionlimit(10**8)

def dfs(v, visited, NG, n):
    visited[v] = True

    for i in range(n):
        if v & (1 << i):
            continue
        if visited[v | (1 << i)]:
            continue
        if (v | (1 << i)) in NG:
            continue
        dfs(v | (1 << i), visited, NG, n)
            

def solve():
    n = int(input())
    s = input()
    NG = set()
    for i in range(2**n-1):
        if s[i] == '1':
            NG.add(i+1)

    visited = [False] * (2**n)
    dfs(0, visited, NG, n)

    if visited[2**n - 1]:
        print('Yes')
    else:
        print('No')

t = int(input())
for _ in range(t):
    solve()