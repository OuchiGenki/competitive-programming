from bisect import bisect_left, bisect_right

N = int(input())
K = []
A = []
for i in range(N):
    li = list(map(int, input().split()))
    K.append(li[0])
    A.append(li[1:])

for i in range(N):
    A[i].sort()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        tmp = 0
        for k in range(K[i]):
            tmp += bisect_right(A[j], A[i][k])- bisect_left(A[j], A[i][k])
        ans = max(ans, tmp/(K[i]*K[j]))

print(ans)
