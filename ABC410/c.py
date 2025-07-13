N, Q = map(int, input().split())
A = [i+1 for i in range(N)]
base = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1], query[2]
        A[(base + p - 1) % N] = x
    elif query[0] == 2:
        p = query[1]
        print(A[(base + p - 1) % N])
    else:
        k = query[1]
        base = (base + k) % N