N = int(input())
S = list(input())

c1 = 0
for i in range(N):
    if S[i] == '1':
        c1 += 1

now = 0
ans = 0
for i in range(N):
    if S[i] == '1':
        now += 1
    else:
        ans += min(now, c1 - now)

print(ans)