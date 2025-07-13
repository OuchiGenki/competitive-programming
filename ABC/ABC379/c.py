N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

XA = []
for i in range(M):
    XA.append([X[i], A[i]])
XA.sort()

if XA[0][0] != 1 or sum(A) != N:
    print(-1)
    exit()

k = 0
answer = 0
for i in range(M):
    x, a = XA[i]
    if i-1 >= 0:
        k -= XA[i][0]-XA[i-1][0]+1
    if a > 1:
        k += a-1
    print("k", k)
    answer += k

print(answer)