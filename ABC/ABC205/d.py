from bisect import bisect_left

n, q = map(int, input().split())
A = list(map(int, input().split()))
C = [A[0]-1]
for i in range(1, n):
    C.append(C[i-1] + (A[i] - A[i-1] - 1))
for _ in range(q):
    k = int(input())
    if C[n-1] < k:
        print(A[n-1] + k - C[n-1])
    else:
        idx = bisect_left(C, k)
        if idx == 0:
            print(k)
        else:
            print(A[idx-1] + k - C[idx-1])