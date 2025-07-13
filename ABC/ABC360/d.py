from bisect import bisect_right

N, T = map(int, input().split())
S = list(input())
X = list(map(int, input().split()))

F = []
B = []
for i in range(N):
    if S[i] == '1':
        F.append(X[i])
    else:
        B.append(X[i])
F.sort()
B.sort()

cnt = 0
for i in range(len(F)):
    cnt += bisect_right(B, F[i]+2*T) - bisect_right(B, F[i])

print(cnt)