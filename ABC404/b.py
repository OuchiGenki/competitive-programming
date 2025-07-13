from copy import deepcopy

N = int(input())
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(N)]

def rotate(S):
    A = deepcopy(S)
    for i in range(N):
        for j in range(N):
            A[j][N-i-1] = S[i][j]
    
    return A

ans = 10**6
for k in range(4):
    cng = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                cng += 1
    ans = min(ans, cng+k)
    S = rotate(S)

print(ans)
