N = int(input())
S = input()
cnt1 = 0
for i in range(N):
    if S[i] == '1':
        cnt1 += 1
now1, ans = 0, 0
for i in range(N):
    if S[i] == '1':
        now1 += 1
        continue
    ans += min(now1, cnt1 - now1)
print(ans)