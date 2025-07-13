import sys
sys.setrecursionlimit(10**8)

N = int(input())
A = [[list(map(int, input().split())) for i in range(N)] for j in range(N)]
Q = int(input())

cumsum = [[[0 for i in range(N+1)] for j in range(N+1)] for k in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            cumsum[i][j][k] += cumsum[i-1][j][k]
            cumsum[i][j][k] += cumsum[i][j-1][k]
            cumsum[i][j][k] += cumsum[i][j][k-1]
            cumsum[i][j][k] -= cumsum[i-1][j-1][k]
            cumsum[i][j][k] -= cumsum[i][j-1][k-1]
            cumsum[i][j][k] -= cumsum[i-1][j][k-1]
            cumsum[i][j][k] += cumsum[i-1][j-1][k-1]
            cumsum[i][j][k] += A[i-1][j-1][k-1]

ans = []
for i in range(Q):
    lx, rx, ly, ry, lz, rz = map(lambda x: int(x)-1, input().split())
    ans.append(cumsum[rx+1][ry+1][rz+1] - cumsum[lx][ry+1][rz+1] - cumsum[rx+1][ly][rz+1] - cumsum[rx+1][ry+1][lz] + cumsum[lx][ly][rz+1] + cumsum[rx+1][ly][lz] + cumsum[lx][ry+1][lz] - cumsum[lx][ly][lz])

for i in ans:
    print(i)