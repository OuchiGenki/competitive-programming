from bisect import bisect_left

n, q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
sumA = sum(A)
cum = [0]
for i in range(n):
    cum.append(cum[-1] + A[i])

for i in range(q):
    b = int(input())
    idx = bisect_left(A, b-1)
    x = cum[idx] + (b-1) * (n-idx)
    if x+1 <= sumA:
        print(x+1)
    else:
        print(-1)