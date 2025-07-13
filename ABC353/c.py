N = int(input())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(N):
    res += (N-1) * A[i]

def bs(x, left):
    ng = left
    ok = N
    while ok-ng > 1:
        mid = (ok+ng)//2
        y = A[mid]
        if x + y >= 10**8:
            ok = mid
        else:
            ng = mid
    
    return ok

for i in range(N):
    k = N - bs(A[i], i)
    res -= 10**8*k

print(res)