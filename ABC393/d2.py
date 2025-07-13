from collections import defaultdict

N = int(input())
S = list(input())
c1 = 0
for i in range(N):
    if S[i] == '1':
        c1 += 1

ans = 0
cnt = 0
for i in range(N):
    if S[i] == '1':
        cnt += 1
        continue
    ans += min(cnt, c1-cnt)
print(ans)