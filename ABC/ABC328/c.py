N, Q = map(int, input().split())
S = input()
cnt = [[0 for i in range(N)] for j in range(26)]

for i in range(26):
    c = chr(ord('a') + i)
    tmp = 0
    for j in range(1, N):
        if S[j] == S[j-1] == c:
            tmp += 1
        cnt[i][j] = tmp

for i in range(Q):
    l, r = map(int, input().split())
    ans = 0
    for j in range(26):
        ans += cnt[j][r-1] - cnt[j][l-1]
    print(ans)