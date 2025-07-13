from bisect import bisect_right

def f(x):
    i = bisect_right(A, x)
    if i % 2 == 0:
        return B[i-1] + x - A[i-1]
    else:
        return B[i-1]

N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(N)]
cnt = 0
for i in range(2, N):
    if i % 2 == 0:
        cnt += A[i] - A[i-1]
    B[i] = cnt

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(f(r) - f(l))