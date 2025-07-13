N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())
dp = [False] * (X+1)
dp[0] = True
for i in range(X):
    if not dp[i] or i in B:
        continue
    for j in range(N):
        if i + A[j] < X+1:
            dp[i+A[j]] = True
if dp[X]:
    print('Yes')
else:
    print('No')