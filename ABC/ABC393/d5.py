N = int(input())
S = input()
cnt1 = 0
for i in range(N):
    if S[i] == '1':
        cnt1 += 1

ans = 0
now = 0
for i in range(N):
    if S[i] == '1':
        now += 1
    else:
        ans += min(now, cnt1- now)
print(ans)