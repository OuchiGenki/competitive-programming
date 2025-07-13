from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort(reverse=True)


def bs(x):
    global ok, ng
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if B[mid] >= x:
            ok = mid
        else:
            ng = mid
    return ok


ok = -1
ng = len(B)
answer = defaultdict(lambda: -1)
for i in range(N):
    a = ok
    x = bs(A[i])
    print("a:",a," x:", x)

    if x == a:
        ok = x
        ng = len(B)
        continue

    for j in range(len(answer), x+1):
        answer[B[j]] = i+1
    
    ok = x
    ng = len(B)


    
for i in range(M):
    print(answer[B[i]])