def solve():
    N = int(input())
    S = list(map(int, input().split()))
    S = [S[0]] + sorted(S[1:-1]) + [S[-1]]
    ans = 1
    domino = S[0]
    idx = 1
    while True:
        if domino * 2 >= S[-1]:
            ans += 1
            print(ans)
            break

        while domino * 2 >= S[idx]:
            idx += 1

        if domino == S[idx-1]:
            print(-1)
            break

        domino = S[idx-1]
        ans += 1


T = int(input())
for i in range(T):
    solve()