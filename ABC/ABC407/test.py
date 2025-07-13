H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

tmp = 0
for i in range(H):
    for j in range(W):
        tmp ^= A[i][j]
print(tmp)