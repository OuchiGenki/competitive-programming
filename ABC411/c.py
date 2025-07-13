N, Q = map(int, input().split())
A = list(map(int, input().split()))
G = [0 for i in range(N)]
ans = 0

for i in range(Q):
    a = A[i]-1
    if N == 1:
        G[0] ^= 1
        print(G[0])
        continue

    if a == 0:
        if G[a] == 0 and G[a+1] == 0:
            ans += 1
            G[a] = 1
        elif G[a] == 0 and G[a+1] == 1:
            G[a] = 1
        elif G[a] == 1 and G[a+1] == 0:
            ans -= 1
            G[a] = 0
        elif G[a] == 1 and G[a+1] == 1:
            G[a] = 0
        print(ans)
        continue

    if a == N-1:
        if G[a] == 0 and G[a-1] == 0:
            ans += 1
            G[a] = 1
        elif G[a] == 0 and G[a-1] == 1:
            G[a] = 1
        elif G[a] == 1 and G[a-1] == 0:
            ans -= 1
            G[a] = 0
        elif G[a] == 1 and G[a-1] == 1:
            G[a] = 0
        print(ans)
        continue

    if G[a] == 0 and G[a-1] == 0 and G[a+1] == 0:
        ans += 1
        G[a] = 1
    elif G[a] == 0 and G[a-1] == 1 and G[a+1] == 0:
        G[a] = 1
    elif G[a] == 0 and G[a-1] == 0 and G[a+1] == 1:
        G[a] = 1
    elif G[a] == 0 and G[a-1] == 1 and G[a+1] == 1:
        ans -= 1
        G[a] = 1

    elif G[a] == 1 and G[a-1] == 0 and G[a+1] == 0:
        ans -= 1
        G[a] = 0
    elif G[a] == 1 and G[a-1] == 1 and G[a+1] == 0:
        G[a] = 0
    elif G[a] == 1 and G[a-1] == 0 and G[a+1] == 1:
        G[a] = 0
    elif G[a] == 1 and G[a-1] == 1 and G[a+1] == 1:
        ans += 1
        G[a] = 0
    
    print(ans)