from sortedcontainers import SortedList

def bs(B, a, m):
    ng = -1
    ok = len(B)
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if a + B[mid] >= m:
            ok = mid
        else:
            ng = mid
    return ok


def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = SortedList(B)
    A.sort()
    ans = 0
    usedA = [False] * n
    for i in range(n):
        idx = bs(B, A[i], m)
        if idx == len(B):
            continue
        ans += (A[i] + B[idx]) % m
        usedA[i] = True
        B.remove(B[idx])
    bi = 0
    for i in range(len(A)):
        if usedA[i]:
            continue
        ans += A[i] + B[bi]
        bi += 1    
    print(ans)
    
        

t = int(input())
for _ in range(t):
    solve()