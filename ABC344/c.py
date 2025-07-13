N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

s = set()
for i in range(N):
    for j in range(M):
        for k in range(L):
            s.add(A[i] + B[j] + C[k])

for i in range(Q):
    if X[i] in s:
        print('Yes')
    else:
        print('No')