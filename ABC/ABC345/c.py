S = list(input())
N = len(S)
cnt = [0 for i in range(26)]
flag = False
for i in range(N):
    cnt[ord(S[i]) - ord('a')] += 1
    if cnt[ord(S[i]) - ord('a')] > 1:
        flag = True

res = N*(N-1)//2
for i in range(26):
    res -= cnt[i]*(cnt[i]-1)//2

if flag:
    res += 1

print(res)